# Copyright (c) 2013, saheeth and contributors
# For license information, please see license.txt
from multiprocessing import Condition
import frappe
from frappe.utils import data
def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)
	print(data, columns)
	return columns, data

def get_columns(filters):
	columns = []
	if 'ts_movable_type' in filters:
		if filters['ts_movable_type'] == 'Precious Metal':
			columns = [
				{
					"label": ("Material type"),
					"fieldtype": "Select",
					"fieldname": "type",
					"options":['Gold','Silver','Platinum','Diamond'],
					"width": 130
				},
				{
					"label": ("Metal Model"),
					"fieldtype": "Select",
					"fieldname": "metal_model",
					"options": ['Bangle','Ring','Chain'],
					"width": 130
				},
				{
					"label": ("Quantity Type"),
					"fieldtype": "Select",
					"fieldname": "quantity_type",
					"options": ['Kilogram','Gram','Pavan'],
					"width": 130
				},
				{
					"label": ("Measured Quantity"),
					"fieldtype": "Float",
					"fieldname": "measured_quantity",
					"width": 130
				},
				{
					"label": ("Purchase Rate"),
					"fieldtype": "Currency",
					"fieldname": "ts_pur_rate",
					"width": 130
				},
				{
					"label": ("Purchase Date"),
					"fieldtype": "Date",
					"fieldname": "ts_pur_date",
					"width": 130
				},
				{
					"label": ("Purchase Shop Name"),
					"fieldtype": "Data",
					"fieldname": "ts_pur_sh_name",
					"width": 200
				},
				{
					"label": ("Purchase Shop Place"),
					"fieldtype": "Data",
					"fieldname": "ts_pur_sh_place",
					"width": 200
				}
			]
		if filters['ts_movable_type'] == 'Vehicle':
			columns = [{
					"label": (" Vehicle Type"),
					"fieldtype": "Select",
					"fieldname": "ts_vehicle_type",
					"options":['Two Wheeler','Four Wheeler','Heavy Vehicle'],
					"width": 200
				},
				{
					"label": (" Vehicle Name"),
					"fieldtype": "Data",
					"fieldname": "ts_vehicle_name",
					"width": 200
				},
				{
					"label": (" Vehicle Number"),
					"fieldtype": "Data",
					"fieldname": "ts_vehicle_number",
					"width": 200
				}]
		if filters['ts_movable_type'] == 'Liquid Cash':
			columns = [
				{
					"label": (" Cash Details"),
					"fieldtype": "Select",
					"options":['Cash In','Cash Out'],
					"fieldname": "cash_details",
					"width": 200
				},
				{
					"label": ("Cash in Date"),
					"fieldtype": "Date",
					"fieldname": "cash_in_date",
					"width": 200
				},
				{
					"label": (" Cash In Amount"),
					"fieldtype": "Currency",
					"fieldname": "cash_in",
					"width": 200
				}]
		if filters['ts_movable_type'] == 'Home Appliances':
			columns = [
				{
					"label": ("Appliance Name"),
					"fieldtype": "Data",
					"fieldname": "appliance_name",
					"width": 200
				},
				{
					"label": ("Purchase Rate"),
					"fieldtype": "Currency",
					"fieldname": "purchase_rate",
					"width": 200
				},
				{
					"label": (" Purchase Date and Time"),
					"fieldtype": "Datetime",
					"fieldname": "purchase_date_and_time",
					"width": 200
				},
				{
					"label": ("Purchase Bill Image"),
					"fieldtype": "Image",
					"fieldname": "purchase_bill_image",
					"width": 200
				},
				{
					"label": ("purchase Shop Name"),
					"fieldtype": "Data",
					"fieldname": "purchase_shop_name",
					"width": 200
				},
				{
					"label": ("Appliance Type"),
					"fieldtype": "Select",
					"options":['Warranty','Non-Warranty'],
					"fieldname": "appliance_type",
					"width": 200
				},
				{
					"label": ("Warranty Date"),
					"fieldtype": "Date",
					"fieldname": "warranty_date",
					"width": 200
				}
				]
		if filters['ts_movable_type'] == 'Function':
			columns = [
				{
					"label": ("Function Category"),
					"fieldtype": "Select",
					"fieldname": "function_category",
					"options" : ['Visiting','Organize'],
					"width": 200
				},
				{
					"label": ("Function Name"),
					"fieldtype": "Data",
					"fieldname": "function_name",
					"width": 200
				},
				{
					"label": ("Function Date"),
					"fieldtype": "Date",
					"fieldname": "function_date",
					"width": 200
				},
				{
					"label": ("Person Name"),
					"fieldtype": "Data",
					"fieldname": "person_name",
					"width": 200
				},
				{
					"label": ("Relative Category"),
					"fieldtype": "Data",
					"fieldname": "relative_category",
					"width": 200
				},
				{
					"label": ("Gift Purchased"),
					"fieldtype": "Select",
					"fieldname": "gift_purchased",
					"options":['Purchase','Not Purchase'],
					"width": 200
				},
				{
					"label": ("Gift Type"),
					"fieldtype": "Select",
					"fieldname": "gift_type",
					"options":['Cash','Things'],
					"width": 200
				},
				{
					"label": ("Amount Given"),
					"fieldtype": "Currency",
					"fieldname": "amount_given",
					"width": 200
				},
				{
					"label": ("Gift By"),
					"fieldtype": "Data",
					"fieldname": "gift_by",
					"width": 200
				},
				{
					"label": ("Catering Name"),
					"fieldtype": "Data",
					"fieldname": "catering_name",
					"width": 200
				},
				{
					"label": ("Catering Phone Number"),
					"fieldtype": "Int",
					"fieldname": "catering_phone_number",
					"width": 200
				},
				{
					"label": ("Catering Cost"),
					"fieldtype": "Currency",
					"fieldname": "catering_cost",
					"width": 200
				},
				{
					"label": ("Purchased Price"),
					"fieldtype": "Currency",
					"fieldname": "purchased_price",
					"width": 200
				},
				{
					"label": ("Total Price "),
					"fieldtype": "Currency",
					"fieldname": "total_price",
					"width": 200
				},]
	if 'ts_property_type' in filters:
		if filters['ts_property_type'] == 'Agriculture Land':
			columns = [
				{
					"label": ("Location"),
					"fieldtype": "Data",
					"fieldname": "location",
					"width": 130
				},
				{
					"label": ("Area Measurement"),
					"fieldtype": "Select",
					"fieldname": "area_type",
					"options": ['Acre','sq.ft'],
					"width": 130
				},
				{
					"label": ("Area Measured"),
					"fieldtype": "Float",
					"fieldname": "area_measured",
					"width": 130
				},
				{
					"label": ("Document Type"),
					"fieldtype": "Select",
					"fieldname": "document_type",
					"options":['Patta','Chitta','Panchayat Tax Receipt'],
					"width": 130
				},
				{
					"label": ("Purchase Cost"),
					"fieldtype": "Currency",
					"fieldname": "purchase_cost",
					"width": 130
				},
				{
					"label": ("Registration Date"),
					"fieldtype": "Date",
					"fieldname": "registration_date",
					"width": 130
				},
				{
					"label": ("Payment Mode"),
					"fieldtype": "Select",
					"fieldname": "payment_mode",
					"options" :['Cash','Online','Both'],
					"width": 200
				}]
		if filters['ts_property_type'] == 'Commercial Land':
			columns = [
				{
					"label": ("Location"),
					"fieldtype": "Data",
					"fieldname": "location",
					"width": 130
				},
				{
					"label": ("Area Measurement"),
					"fieldtype": "Select",
					"fieldname": "area_type",
					"options": ['Acre','sq.ft'],
					"width": 130
				},
				{
					"label": ("Area Measured"),
					"fieldtype": "Float",
					"fieldname": "area_measured",
					"width": 130
				},
				{
					"label": ("Document Type"),
					"fieldtype": "Select",
					"fieldname": "document_type",
					"options":['Patta','Chitta','Panchayat Tax Receipt'],
					"width": 130
				},
				{
					"label": ("Purchase Cost"),
					"fieldtype": "Currency",
					"fieldname": "purchase_cost",
					"width": 130
				},
				{
					"label": ("Registration Date"),
					"fieldtype": "Date",
					"fieldname": "registration_date",
					"width": 130
				},
				{
					"label": ("Payment Mode"),
					"fieldtype": "Select",
					"fieldname": "payment_mode",
					"options" :['Cash','Online','Both'],
					"width": 200
				}]
		if filters['ts_property_type'] == 'Residential Land':
			columns = [
				{
					"label": ("Location"),
					"fieldtype": "Data",
					"fieldname": "location",
					"width": 130
				},
				{
					"label": ("Area Measurement"),
					"fieldtype": "Select",
					"fieldname": "area_type",
					"options": ['Acre','sq.ft'],
					"width": 130
				},
				{
					"label": ("Area Measured"),
					"fieldtype": "Float",
					"fieldname": "area_measured",
					"width": 130
				},
				{
					"label": ("Document Type"),
					"fieldtype": "Select",
					"fieldname": "document_type",
					"options":['Patta','Chitta','Panchayat Tax Receipt'],
					"width": 130
				},
				{
					"label": ("Purchase Cost"),
					"fieldtype": "Currency",
					"fieldname": "purchase_cost",
					"width": 130
				},
				{
					"label": ("Registration Date"),
					"fieldtype": "Date",
					"fieldname": "registration_date",
					"width": 130
				},
				{
					"label": ("Payment Mode"),
					"fieldtype": "Select",
					"fieldname": "payment_mode",
					"options" :['Cash','Online','Both'],
					"width": 200
				}]
	return columns

def get_data(filters):
	conditions = {"ts_asset_type":filters['ts_asset_type']}
	fields = []
	if 'ts_movable_type' in filters:
		conditions['ts_movable_type'] = filters['ts_movable_type']
		if filters['ts_movable_type'] == 'Precious Metal':
			fields =  ['type', 'metal_model', 'quantity_type']
		if filters['ts_movable_type'] == 'Vehicle':
			fields =  ['ts_vehicle_type','ts_vehicle_name','ts_vehicle_number']
		if filters['ts_movable_type'] == 'Liquid Cash':
			fields =  ['cash_details','cash_in_date','cash_in']
		if filters['ts_movable_type'] == 'Home Appliances':
			fields =  ['appliance_name','purchase_rate','purchase_date_and_time','purchase_bill_image','purchase_shop_name','appliance_type','warranty_date']
		if filters['ts_movable_type'] == 'Function':
			fields =  ['function_category', 'function_name','function_date','person_name','relative_category','gift_purchased','gift_type','amount_given','gift_by','catering_name','catering_phone_number','catering_cost','purchased_price','total_price']

	if 'ts_property_type' in filters:
		conditions['ts_property_type'] = filters['ts_property_type']
		fields =  ['location', 'area_type', 'area_measured','document_type','purchase_cost','registration_date','payment_mode']
	if fields:
		final_data = frappe.get_all('TS Asset', conditions,fields)
		return final_data
	return []
	