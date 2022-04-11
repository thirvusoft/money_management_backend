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
			giftaadhar=doc.ts_aadhar_no
			if giftaadhar or giftaadhar==0:
				if not giftaadhar.isdigit() or len(giftaadhar) != 16:
					frappe.throw(frappe._("Invalid Aadhar Number. {0} is not 16 digit.").format(giftaadhar), frappe.InvalidPhoneNumberError)
		elif doc.subtype_name == "Interest Collection":
			interestaadhar=doc.ts_interest_aadhar_no
			if interestaadhar or interestaadhar==0:
				if not interestaadhar.isdigit() or len(interestaadhar) != 16:
					frappe.throw(frappe._("Invalid Aadhar Number. {0} is not 16 digit.").format(interestaadhar), frappe.InvalidPhoneNumberError)
		else :
			pass