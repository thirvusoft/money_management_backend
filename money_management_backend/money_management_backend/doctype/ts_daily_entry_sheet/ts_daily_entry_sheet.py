
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import date
class TSDailyEntrySheet(Document):
	def after_insert(self):
		return
		credit_account=frappe.db.get_single_value('TS Settings','account_to_credit')
		company=frappe.db.get_single_value('Global Defaults','default_company')
		account= frappe.get_value("TS Subtype", self.sub_type,"account")
		if(account==None):
			frappe.throw(f'Account {account} does not exist')
		doc=frappe.new_doc("Journal Entry")
		acc=[{
			"account": account,
			"debit_in_account_currency":self.amount
		},
		{
			"account": credit_account,
			"credit_in_account_currency":self.amount
		}
		]
		doc.update({
			"company":company,
			"voucher_type":"Journal Entry",
			"posting_date":date.today(),
			"accounts": acc
			})

		doc.insert()
		doc.submit()
		frappe.db.commit()
