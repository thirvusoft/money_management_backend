# Copyright (c) 2022, saheeth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TSVehicleNumber(Document):
	def validate(doc):
		vehicle=doc.vehicle_number
		if not vehicle.isdigit() or len(vehicle) != 10:
			frappe.throw(frappe._("Invalid Vehicle Number. {0} is not 10 digit.").format(vehicle), frappe.InvalidPhoneNumberError)
		else :
			pass
		