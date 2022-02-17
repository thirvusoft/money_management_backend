
import frappe
from frappe.auth import LoginManager
from frappe.utils.response import build_response
from frappe.utils import getdate, nowdate
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
			"mobile_no": user_doc.mobile_no,
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

def create_asset_doc(doc):
	a = frappe.new_doc("TS Asset")
	if doc['ts_asset_type']=="Movable":
		if doc['ts_movable_type'] =="Precious Metal":
			a.metal_model=doc["metal_model"]
			a.quantity_type=doc["quantity_type"]
			a.measured_quantity=doc["measured_quantity"]
			a.ts_pur_rate=doc["ts_pur_rate"]
			a.ts_pur_sh_name=doc["ts_pur_sh_name"]
			a.ts_pur_sh_place=doc["ts_pur_sh_place"]
			a.ts_pur_date =doc["ts_pur_date"]
		if doc['ts_movable_type'] =="Vehicle":
			a.ts_vehicle_type=doc["ts_vehicle_type"]
			a.ts_vehicle_name=doc["ts_vehicle_name"]
			a.ts_vehicle_number=doc["ts_vehicle_number"]
		if doc['ts_movable_type'] =="Liquid Cash":
			a.cash_details=doc["cash_details"]
			a.cash_in_date=doc["cash_in_date"]
			a.cash_in=doc["cash_in"]
		if doc['ts_movable_type'] =="Home Appliances":
			a.appliance_name=doc["appliance_name"]
			a.purchase_rate=doc["purchase_rate"]
			a.purchase_date_and_time=doc["purchase_date_and_time"]
			a.purchase_bill_image=doc["purchase_bill_image"]
			a.purchase_shop_name=doc["purchase_shop_name"]
			a.appliance_type=doc["appliance_type"]
			a.warranty_date=doc["warranty_date"]
		if doc['ts_movable_type'] =="Function":
			a.function_category=doc["function_category"]
			a.function_name=doc["function_name"]
			a.function_date=doc["function_date"]
			a.person_name=doc["person_name"]
			a.relative_category=doc["relative_category"]
			a.gift_purchased=doc["gift_purchased"]
			a.gift_type=doc["gift_type"]
			a.amount_given=doc["amount_given"]
			a.gift_by=doc["gift_by"]
			a.catering_name=doc["catering_name"]
			a.catering_phone_number=doc["catering_phone_number"]
			a.catering_cost=doc["catering_cost"]
			a.purchased_price=doc["purchased_price"]
			a.total_price=doc["total_price"]
	a.insert()


@frappe.whitelist()
def get_all(movable_type):
	if movable_type == "Precious Metal":
		fields = ['type','metal_model','quantity_type','measured_quantity','ts_pur_rate','ts_pur_sh_name','ts_pur_sh_place','ts_pur_date']
	if movable_type == "Vehicle":
		fields = ['ts_vehicle_type','ts_vehicle_name','ts_vehicle_number']
	if movable_type == "Liquid Cash":
		fields = ['cash_details','cash_in_date','cash_in']
	if movable_type == "Home Appliances":
		fields = ['appliance_name','purchase_rate','purchase_date_and_time','purchase_bill_image','purchase_shop_name','appliance_type','warranty_date']
	if movable_type == "Function":
		fields = ['function_category', 'function_name','function_date','person_name','relative_category','gift_purchased','gift_type','amount_given','gift_by','catering_name','catering_phone_number','catering_cost','purchased_price','total_price']
	final_data=frappe.get_all(
		'TS Asset',
		filters = {'ts_movable_type': movable_type}, fields=fields)
	return final_data