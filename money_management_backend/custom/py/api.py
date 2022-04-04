from dataclasses import fields
from pydoc import doc
import frappe
from frappe.auth import LoginManager
from frappe.utils.response import build_response
import json
from frappe.handler import upload_file
def generate_token(user):
	user_details = frappe.get_doc("User", user)
	api_key = user_details.api_key
	api_secret = frappe.generate_hash(length=15)
	# if api key is not set generate api key
	if not user_details.api_key:
		api_key = frappe.generate_hash(length=15)
		user_details.api_key = api_key
	user_details.api_secret = api_secret
	user_details.save(ignore_permissions=True)

	return f'token {api_key}:{api_secret}'

@frappe.whitelist(allow_guest=True)
def login():
	req = frappe.local.form_dict
	try:
		frappe.db.begin()
		login_manager = LoginManager()
		login_manager.authenticate(req.email, req.password)
		token = generate_token(login_manager.user)
		frappe.local.response.http_status_code = 200
		frappe.local.response["message"] = "Logged In Successfully"
		frappe.local.response["token"] = token
		ts_subtype = frappe.get_all("TS Subtype", filters={"ts_type":"Asset","ts_subtype":['!=',""],"fromfe":1},fields=["ts_subtype","icon_code","Name"], as_list = 1)
		final_ts_subtype_list = []
		for val in ts_subtype:
			val = list(val)
			val.append(val[0][0].upper())
			final_ts_subtype_list.append(val)

		frappe.local.response["asset"] = final_ts_subtype_list
		frappe.db.commit()

		
		
	except frappe.AuthenticationError as e:
		frappe.db.rollback()
		if not frappe.db.exists('User', req.email):
			frappe.local.response.http_status_code = 401
			frappe.local.response["message"] = "User Not Found"
		else:
			frappe.local.response.http_status_code = 401
			frappe.local.response["message"] = "Invalid Password"

	except frappe.SecurityException as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 403
		frappe.local.response["message"] = "You do not have enough permission to access this server"

	except frappe.ValidationError as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 417
		frappe.local.response["message"] = "Validation Failed"

	except frappe.SessionStopped as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 503
		frappe.local.response["message"] = "Your Session was Expired"		
	
	except Exception:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 500
		frappe.local.response["message"] = "Login Failed"
		frappe.log_error(title=req.cmd, message = f'{str(req)} \n {frappe.get_traceback()}')

	finally:
		return build_response('json')
	


#Daily Entry
@frappe.whitelist()
def daily_entry_submit(type, subtype,name,notes,amount,remainder_date=None):
	req = frappe.local.form_dict
	try:
		frappe.get_doc("TS Daily Entry Sheet",name)
		frappe.local.response.http_status_code = 409
		frappe.local.response["message"] = "File already exists with this name"
		return build_response('json')
	except:
		pass
	doc=frappe.new_doc("TS Daily Entry Sheet")
	doc.update(
		{	
		"type":type,
		"sub_type":subtype,
		"entry_name":name,
		"notes":notes,
		"amount":amount,
		"remainder_date":remainder_date
		}),
	
	try:
		doc.insert(ignore_permissions=True)
		frappe.db.commit()
		frappe.local.response["message"]="Success"
		frappe.local.response["docname"]=doc.name
		
		
	except frappe.ValidationError as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 417
		frappe.local.response["message"] = "Validation Failed"
	
	except frappe.PermissionError as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 403
		frappe.local.response["message"] = "You do not have enough permission to access this server"

    	
	except Exception:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 500
		frappe.local.response["message"] ="Couldn't Save the file"
		frappe.log_error(title=req.cmd, message = f'{str(req)} \n {frappe.get_traceback()}')

	finally:
		return build_response('json')	

# Other customization
@frappe.whitelist()
def create_new_subtype(type, subtype, iconbinerycode):
	doc=frappe.new_doc("TS Subtype")
	doc.update(
		{
		"ts_type":type,
		"ts_subtype":subtype,
		"icon_code":iconbinerycode,
		"fromfe":1
		})
	
	try:
		doc.insert(ignore_permissions=True)
		frappe.db.commit() 
		frappe.local.response.http_status_code = 200
		frappe.local.response["message"] = "Entered Successfully"
	except frappe.InternalServerError as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 500
		frappe.local.response["message"] = "Server Error"	
	except frappe.InternalServerError as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 550
		frappe.local.response["message"] = "Name Already Exist"	


	except frappe.ValidationError as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 417
		frappe.local.response["message"] = "Validation Failed"

	
	finally:
		return build_response('json')		

#With subtype
@frappe.whitelist()
def subtype_list (type):
	docs = frappe.get_all("TS Subtype", filters={"ts_type":type,"ts_subtype":['!=',""],"fromfe":1},fields=["ts_subtype","icon_code","Name"], as_list = 1)
	final_list = []
	for doc in docs:
		doc = list(doc)
		doc.append(doc[0][0].upper())
		final_list.append(doc)

	frappe.local.response[type]= final_list
			
	

#With and Without Subtype
@frappe.whitelist()
def icon_list (type):
	docs = frappe.get_all("TS Subtype", filters={"ts_type":type,"fromfe":1},fields=["icon_code"], as_list = 1)
	frappe.local.response[type]= docs





#Profile
@frappe.whitelist()
def get_profile_data(email):
	try:
		user_doc = frappe.get_doc("User", email)
		response={
				"email": user_doc.email,
				"full_name": user_doc.full_name,
				"mobile_number": user_doc.mobile_no
			}
		frappe.local.response["message"]= response
	except frappe.DoesNotExistError:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 404
		frappe.local.response["message"] = "User Not Found"
	finally:
		return build_response('json')