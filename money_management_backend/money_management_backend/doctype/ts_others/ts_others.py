# Copyright (c) 2022, saheeth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TSOthers(Document):
	def validate(doc):
		aadhar=doc.ts_aadhar
		if not aadhar.isdigit() or len(aadhar) != 16:
			frappe.throw(frappe._("Invalid Aadhar Number. {0} is not 16 digit.").format(aadhar), frappe.InvalidPhoneNumberError)
		else :
			pass