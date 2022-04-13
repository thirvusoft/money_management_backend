# Copyright (c) 2022, Thirvusoft and contributors
# For license information, please see license.txt

from ast import Pass
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

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
		elif self.sub_type_name == "Interest Collection":
			interest_aadhar=self.ts_iaadhar_no
			if interest_aadhar or interest_aadhar==0:
				if not interest_aadhar.isdigit() or len(interest_aadhar) != 16:
					frappe.throw(frappe._("Invalid Aadhar Number. {0} is not 16 digit.").format(interest_aadhar), frappe.InvalidPhoneNumberError)
		elif self.sub_type_name != ["Business Profit","Dividends","Lottery","Rental","Asset/Scrap Sale","Salary","Revenue","Dividend","Lottery","Coupons","Refunds","Rental","Scrap Sale","Asset Sale","Salary","Commercial Land","Residential Land","Agricultural Land","Machinery","Home Appliance","Vehicle","Diamond","Platinum","Silver","Gold", "EMI","Debt"]:
			aadhar_no=self.ts_aadhar_number
			if aadhar_no or aadhar_no==0:
				if not aadhar_no.isdigit() or len(aadhar_no) != 16:
					frappe.throw(frappe._("Invalid Aadhar Number. {0} is not 16 digit.").format(aadhar_no), frappe.InvalidPhoneNumberError)
		else:
			Pass

	def autoname(doc):
		if doc.ts_entry_type == "Income": 
			doc.name = make_autoname(doc.ts_entry_type + ".####")
		elif doc.ts_entry_type == "Asset": 
			doc.name = make_autoname(doc.ts_entry_type + ".####")
		elif doc.ts_entry_type == "Liability": 
			doc.name = make_autoname(doc.ts_entry_type + ".####")



