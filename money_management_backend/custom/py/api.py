
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

@frappe.whitelist()
def create_asset_doc(doc):
	doc = json.loads(doc)
	a = frappe.new_doc("TS Asset")
	a.ts_asset_type = doc['ts_asset_type']
	if doc.get('ts_asset_type', None)=="Portable":
		if doc.get('ts_Portable_type', None) =="Precious Metal":
			a.metal_model=doc.get("metal_model", None)
			a.quantity_type=doc.get("quantity_type", None)
			a.measured_quantity=doc.get("measured_quantity", None)
			a.ts_pur_rate=doc.get("ts_pur_rate", None)
			a.ts_pur_sh_name=doc.get("ts_pur_sh_name", None)
			a.ts_pur_sh_place=doc.get("ts_pur_sh_place", None)
			a.ts_pur_date =doc.get("ts_pur_date", None)
		if doc.get('ts_Portable_type', None) =="Vehicle":
			a.ts_vehicle_type=doc.get("ts_vehicle_type", None)
			a.ts_vehicle_name=doc.get("ts_vehicle_name", None)
			a.ts_vehicle_number=doc.get("ts_vehicle_number", None)
		if doc.get('ts_Portable_type', None) =="Liquid Cash":
			a.cash_details=doc.get("cash_details", None)
			a.cash_in_date=doc.get("cash_in_date", None)
			a.cash_in=doc.get("cash_in", None)
		if doc.get('ts_Portable_type', None) =="Home Appliances":
			a.appliance_name=doc.get("appliance_name", None)
			a.purchase_rate=doc.get("purchase_rate", None)
			a.purchase_date_and_time=doc.get("purchase_date_and_time", None)
			a.purchase_bill_image=doc.get("purchase_bill_image", None)
			a.purchase_shop_name=doc.get("purchase_shop_name", None)
			a.appliance_type=doc.get("appliance_type", None)
			a.warranty_date=doc.get("warranty_date", None)
		if doc.get('ts_Portable_type', None) =="Function":
			a.function_category=doc.get("function_category", None)
			a.function_name=doc.get("function_name", None)
			a.function_date=doc.get("function_date", None)
			a.person_name=doc.get("person_name", None)
			a.relative_category=doc.get("relative_category", None)
			a.gift_purchased=doc.get("gift_purchased", None)
			a.gift_type=doc.get("gift_type", None)
			a.amount_given=doc.get("amount_given", None)
			a.gift_by=doc.get("gift_by", None)
			a.catering_name=doc.get("catering_name", None)
			a.catering_phone_number=doc.get("catering_phone_number", None)
			a.catering_cost=doc.get("catering_cost", None)
			a.purchased_price=doc.get("purchased_price", None)
			a.total_price=doc.get("total_price", None)
	a.insert()


@frappe.whitelist()
def get_all(Portable_type):
	if Portable_type == "Precious Metal":
		fields = ['type','metal_model','quantity_type','measured_quantity','ts_pur_rate','ts_pur_sh_name','ts_pur_sh_place','ts_pur_date']
	if Portable_type == "Vehicle":
		fields = ['ts_vehicle_type','ts_vehicle_name','ts_vehicle_number']
	if Portable_type == "Liquid Cash":
		fields = ['cash_details','cash_in_date','cash_in']
	if Portable_type == "Home Appliances":
		fields = ['appliance_name','purchase_rate','purchase_date_and_time','purchase_bill_image','purchase_shop_name','appliance_type','warranty_date']
	if Portable_type == "Function":
		fields = ['function_category', 'function_name','function_date','person_name','relative_category','gift_purchased','gift_type','amount_given','gift_by','catering_name','catering_phone_number','catering_cost','purchased_price','total_price']
	final_data=frappe.get_all(
		'TS Asset',
		filters = {'ts_Portable_type': Portable_type}, fields=fields)
	return final_data

@frappe.whitelist()
def get_asset_categorywise_total_entries():
	req = frappe.local.form_dict
	try:
		frappe.db.begin()
		final_data = []
		asset_type_key = ''
		if req.asset_type == 'Property':
			asset_type_key = 'ts_property_type'
			entries = frappe.get_list('TS Asset', {'ts_asset_type':req.asset_type}, ['ts_property_type'])
		if req.asset_type == 'Portable':
			asset_type_key = 'ts_Portable_type'
			entries = frappe.get_list('TS Asset', {'ts_asset_type':req.asset_type}, ['ts_Portable_type'])
		for entry in entries:
			if not {entry['ts_property_type']:0} in final_data:
				final_data.append({entry['ts_property_type']:0})
		for data in final_data:
			data[ list(data.keys())[0]] = frappe.db.count('TS Asset', {asset_type_key: list(data.keys())[0]})

		frappe.local.response.http_status_code = 200
		frappe.local.response["message"] = final_data
		frappe.db.commit()
	except:
		frappe.db.rollback()
		frappe.local.response.http_status_code = 500
		frappe.local.response["message"] = 'Unable to fetch records'
	finally:
		return build_response('json')