# Copyright (c) 2022, saheeth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TSSubtype(Document):
	def before_insert(self):
		docs=[i['ts_subtype'] for i in frappe.get_all("TS Subtype", {"fromfe":self.fromfe}, ["ts_subtype"])]
		if self.ts_subtype in docs and self.ts_subtype!="":
			frappe.local.response.http_status_code = 550
			frappe.local.response["Message"]="Name Already Exist"
			frappe.throw("Name Already Exist")
		return	
		if(self.account==None):
			acc=frappe.new_doc('Account')
			acc.update(dict(
				
			))
			acc.save()
			self.account=acc.name
