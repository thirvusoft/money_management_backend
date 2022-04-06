# Copyright (c) 2022, Thirvusoft and contributors
# For license information, please see license.txt

from ast import Pass
import frappe
from frappe.model.document import Document

class TSMoneyManager(Document):
	def validate(self):
		asset=["Vehicle", "Home Appliance", "Machinery", "Agricultural Land", "Commercial Land", "Residential Land"]
		if(self.sub_type_name=='Debt'):
			selleradhar=self.ts_creditor_aadhar_number
			if selleradhar or selleradhar==0:
				if not selleradhar.isdigit() or len(selleradhar) != 16:
					frappe.throw(frappe._("{0} is more or less then 16 digit. Enter a valid Aadhar Number.").format(selleradhar), frappe.InvalidPhoneNumberError)
		elif self.sub_type_name in asset:
			selleradhar=self.ts_seller_aadhar
			if selleradhar or selleradhar==0:
				if not selleradhar.isdigit() or len(selleradhar) != 16:
					frappe.throw(frappe._("{0} is more or less then 16 digit. Enter a valid Aadhar Number.").format(selleradhar), frappe.InvalidPhoneNumberError)
		elif (self.sub_type_name =="Rental"):
			selleradhar=self.ts_raadhar_number
			if selleradhar or selleradhar==0:
				if not selleradhar.isdigit() or len(selleradhar) != 16:
					frappe.throw(frappe._("{0} is more or less then 16 digit. Enter a valid Aadhar Number.").format(selleradhar), frappe.InvalidPhoneNumberError)
		elif (self.sub_type_name =="Asset/Scrap Sale"):
			selleradhar=self.ts_saadhar
			if selleradhar or selleradhar==0:
				if not selleradhar.isdigit() or len(selleradhar) != 16:
					frappe.throw(frappe._("{0} is more or less then 16 digit. Enter a valid Aadhar Number.").format(selleradhar), frappe.InvalidPhoneNumberError)
		else:
			Pass