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
	try:
		frappe.db.begin()
		login_manager = LoginManager()
		login_manager.authenticate(req.email, req.password)
		token = generate_token(login_manager.user)
		frappe.local.response.http_status_code = 200
		frappe.local.response["message"] = "Logged In"
		frappe.local.response["token"] = token
		frappe.local.response["data"] = get_profile(login_manager.user)
		frappe.db.commit()
	
	except frappe.AuthenticationError:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 401

	except frappe.SecurityException as e:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 403
		frappe.local.response["message"] = str(e)
	
	except Exception:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 500
		frappe.local.response["message"] = "Login Failed"
		frappe.log_error(title=req.cmd, message = f'{str(req)} \n {frappe.get_traceback()}')

	finally:
		return build_response('json')