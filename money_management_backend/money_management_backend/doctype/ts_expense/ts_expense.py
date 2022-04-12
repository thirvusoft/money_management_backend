# Copyright (c) 2022, saheeth and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe import _
from frappe.model.document import Document

class TSExpense(Document):
	def validate(doc):
		if doc.subtype_name == "Social Service":
			aadhar=doc.ts_aadhar_number
			if aadhar or aadhar==0:
				if not aadhar.isdigit() or len(aadhar) != 16:
					frappe.throw(frappe._("Invalid Aadhar Number. {0} is not 16 digit.").format(aadhar), frappe.InvalidPhoneNumberError)
		elif doc.subtype_name == "Gift":
			gift_aadhar=doc.ts_aadhar_no
			if gift_aadhar or gift_aadhar==0:
				if not gift_aadhar.isdigit() or len(gift_aadhar) != 16:
					frappe.throw(frappe._("Invalid Aadhar Number. {0} is not 16 digit.").format(gift_aadhar), frappe.InvalidPhoneNumberError)
		else :
			pass