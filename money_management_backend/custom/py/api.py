from dataclasses import fields
from pydoc import doc
import frappe
from frappe.auth import LoginManager
from frappe.utils.response import build_response
import json
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

def get_profile(current_user):
	user_doc = frappe.get_doc("User", current_user)
	return {
			"email": user_doc.email,
			"full_name": user_doc.full_name
		}

@frappe.whitelist(allow_guest=True)
def login():
	req = frappe.local.form_dict
	# docs = frappe.get_list("TS Subtype",fields=["icon"])
	# frappe.local.response[docs]
	
	try:
		frappe.db.begin()
		login_manager = LoginManager()
		login_manager.authenticate(req.email, req.password)
		token = generate_token(login_manager.user)
		frappe.local.response.http_status_code = 200
		frappe.local.response["message"] = "Logged In"
		frappe.local.response["token"] = token
		frappe.local.response["data"] = get_profile(login_manager.user)	
		# docs = frappe.get_all("TS Subtype",filters={"ts_type":"Asset"},fields=["ts_subtype","icon_code"])
		# for i in docs:
		# 	frappe.local.response["Asset"]=docs
		docs = frappe.get_all("TS Subtype", filters={"ts_type":"Asset"},fields=["icon_code"])	
		frappe.local.response["Asset"]= docs
		frappe.db.commit()

		
		
	except frappe.AuthenticationError as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 401
		frappe.local.response["message"] = str(e)

	except frappe.SecurityException as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 403
		frappe.local.response["message"] = str(e)

	except frappe.ValidationError as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 417
		frappe.local.response["message"] = str(e)

	except frappe.SessionStopped as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 503
		frappe.local.response["message"] = str(e)		
	
	except Exception:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 500
		frappe.local.response["message"] = "Login Failed"
		frappe.log_error(title=req.cmd, message = f'{str(req)} \n {frappe.get_traceback()}')

	finally:
		return build_response('json')
	


#apps/money_management_backend/money_management_backend/custom/py/api.py

# Customize

@frappe.whitelist(allow_guest=True)
def daily_entry_submit(Type, Subtype,Name,Notes,Amount,Remainder_date):
	req = frappe.local.form_dict
	doc=frappe.new_doc("TS Daily Entry Sheet")
	doc.update(
		{	
		"type":Type,
		"ts_subtype":Subtype,
		"entry_name":Name,
		"notes":Notes,
		"amount":Amount,
		"remainder_date":Remainder_date
		
		}),
	
	try:
		doc.insert(ignore_permissions=True)
		frappe.local.response.http_status_code = 200
		frappe.local.response["message"] = "success"
		frappe.db.commit()
		
		
	except frappe.ValidationError as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 417
		frappe.local.response["message"] = str(e)

    	
	except Exception:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 500
		frappe.local.response["message"] = "Submit failed"
		frappe.log_error(title=req.cmd, message = f'{str(req)} \n {frappe.get_traceback()}')

	finally:
		return build_response('json')	

# customization
@frappe.whitelist(allow_guest=True)
# def other_entry( Subtype,binaryicon):
# 	doc=frappe.new_doc("TS Subtype")
# 	doc1="Others"
# 	doc.update(
# 		{	
# 		"type":doc1,
# 		"sub_type_name":Subtype,
		# "icon":binaryicon
def custom(Type, Subtype, IconBineryCode):
	req = frappe.local.form_dict
	doc=frappe.new_doc("TS Subtype")
	
	doc.update(
		{
		"ts_type":Type,
		"ts_subtype":Subtype,
		"icon_code":IconBineryCode
		}),
	
	# frappe.local.response.http_status_code = 200
	# frappe.local.response["message"] = "Entered Successfully"
	try:
		duplicate=frappe.db.get_value('TS Subtype', {'ts_subtype':Subtype})
		if duplicate:
			frappe.local.response.http_status_code = 500
			frappe.local.response["message"] = "Duplicate Entry"
		else:
			doc.insert(ignore_permissions=True)
			frappe.db.commit()
			frappe.local.response.http_status_code = 200
			frappe.local.response["message"] = "success"
	except frappe.InternalServerError as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 500
		frappe.local.response["message"] = str(e)	


	except frappe.ValidationError as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 417
		frappe.local.response["message"] = str(e)
	
	except frappe.DuplicateEntryError as e:
		# print("duplicate----------------------------------------------------------------------------------------------************************")
		frappe.local.response["message"] = str(e)
		
	except Exception:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 500
		frappe.local.response["message"] = "Submit failed"
		frappe.log_error(title=req.cmd, message = f'{str(req)} \n {frappe.get_traceback()}')
	
	finally:
		return build_response('json')		


@frappe.whitelist(allow_guest=True)
def subtype (Type):
	docs = frappe.get_all("TS Subtype", filters={"ts_type":Type},fields=["ts_subtype","icon_code"])	
	frappe.local.response[Type]= docs


#Profile
@frappe.whitelist(allow_guest=True)
def profile(email):
    user_doc = frappe.get_doc("User", email)
    return {
            "email": user_doc.email,
            "full_name": user_doc.full_name,
            "mobile_number": user_doc.mobile_no
        }
