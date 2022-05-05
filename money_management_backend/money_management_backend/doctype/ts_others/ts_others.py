# Copyright (c) 2022, saheeth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TSOthers(Document):
	def validate(doc):
		if doc.subtype_name=="Profile":
			aadhar=doc.ts_aadhar
			if aadhar or aadhar==0:
				if not aadhar.isdigit() or len(aadhar) != 12:
					frappe.throw(frappe._("Invalid Aadhar Number. {0} is not 12 digit.").format(aadhar), frappe.InvalidPhoneNumberError)
		elif doc.subtype_name != ["Visiting Card","Profile","Invitation"]:
			aadhar_no=doc.ts_aadhar_no
			if aadhar_no or aadhar_no==0:
				if not aadhar_no.isdigit() or len(aadhar_no) != 12:
					frappe.throw(frappe._("Invalid Aadhar Number. {0} is not 12 digit.").format(aadhar_no), frappe.InvalidPhoneNumberError)
		else :
			pass