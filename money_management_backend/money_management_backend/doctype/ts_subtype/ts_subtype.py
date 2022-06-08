# Copyright (c) 2022, saheeth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TSSubtype(Document):

	def before_insert(self):
		docs=[i['ts_subtype'] for i in frappe.get_all("TS Subtype", {"fromfe":self.fromfe,"ts_type":self.ts_type}, ["ts_subtype"])]
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
    
	# def before_save(self):
	# 	sub_name= self.link_doc_subtype
	# 	frappe.errprint(sub_name)
	# 	link_doc = frappe.get_doc("TS Subtype" , sub_name)
	# 	frappe.errprint(link_doc)
	# 	frappe.errprint(link_doc.ts_type)
	# 	self.link_type = link_doc.ts_type
	# 	frappe.errprint(self.link_type)
	# 	self.link_subtype = link_doc.ts_subtype
	# 	frappe.errprint(self.link_subtype)
	