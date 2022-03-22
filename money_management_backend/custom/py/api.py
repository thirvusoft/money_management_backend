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
def daily_entry_submit(Type, Subtype,Name,Notes,Amount,Remainder_date=None):
	req = frappe.local.form_dict
	try:
		frappe.get_doc("TS Daily Entry Sheet",Name)
		frappe.local.response.http_status_code = 409
		frappe.local.response["message"] = "File already exists with this name"
		return build_response('json')
	except:
		pass
	doc=frappe.new_doc("TS Daily Entry Sheet")
	doc.update(
		{	
		"type":Type,
		"sub_type":Subtype,
		"entry_name":Name,
		"notes":Notes,
		"amount":Amount,
		"remainder_date":Remainder_date
		}),
	
	try:
		doc.insert(ignore_permissions=True)
		frappe.db.commit()
		frappe.local.response["message"]="Success"
		
		
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
def custom(Type , Subtype , IconBineryCode):
	doc=frappe.new_doc("TS Subtype")
	doc.update(
		{
		"ts_type":Type,
		"ts_subtype":Subtype,
		"icon_code":IconBineryCode,
		"fromfe":1
		}),
	
	try:
		doc.insert(ignore_permissions=True)
		frappe.db.commit()
		frappe.local.response.http_status_code = 200
		frappe.local.response["message"] = "Entered Successfully"
	except frappe.InternalServerError as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 500
		frappe.local.response["message"] = "Server Error"	


	except frappe.ValidationError as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 417
		frappe.local.response["message"] = "Validation Failed"

	
	finally:
		return build_response('json')		

#With subtype
@frappe.whitelist()
def withsubtype (Type):
	docs = frappe.get_all("TS Subtype", filters={"ts_type":Type,"ts_subtype":['!=',""],"fromfe":1},fields=["ts_subtype","icon_code","Name"], as_list = 1)
	frappe.local.response[Type]= docs
			
	

#With and Without Subtype
@frappe.whitelist()
def withoutsubtype (Type):
	docs = frappe.get_all("TS Subtype", filters={"ts_type":Type,"fromfe":"1"},fields=["icon_code"])
	frappe.local.response[Type]= docs





#Profile
@frappe.whitelist()
def profile(email):
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


#Image Passing
@frappe.whitelist()
def upload_profile_image():
	req = frappe.local.form_dict
	try:
		frappe.db.begin()
		if not frappe.request.files['file'].__dict__.get('filename',None):
			raise FileNotFoundError
		current_user = frappe.session.user
		frappe.form_dict.doctype = 'User'
		frappe.form_dict.docname = current_user
		frappe.form_dict.fieldname = 'user_image'
		existing_file = frappe.db.get_value('File',{'attached_to_doctype':'User',
						'attached_to_name': current_user, 'attached_to_field': 'user_image'})
		if existing_file:
			frappe.delete_doc("File", existing_file, ignore_permissions=True)
		new_file = upload_file()
		print(new_file)
		frappe.db.set_value('User',current_user,'user_image', new_file.file_url)
		frappe.local.response.http_status_code = 200
		frappe.local.response["message"] = "Image Uploaded Successfully"
		frappe.db.commit()
	except frappe.FileNotFoundError:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 404
		frappe.local.response["message"] = "Kindly Upload a File to Proceed"
	except Exception:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 500
		frappe.local.response["message"] = "Image Upload Failed"
		frappe.log_error(title=req.cmd, message = f'{str(req)} \n {frappe.get_traceback()}')

	finally:
		return build_response('json')