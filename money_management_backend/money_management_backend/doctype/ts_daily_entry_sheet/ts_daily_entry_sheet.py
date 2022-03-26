
# For license information, please see license.txt

import frappe
from frappe.model.document 
import Document
from datetime import date
class TSDailyEntrySheet(Document):
	def after_insert(self):
		account= frappe.get_value("TS Subtype", self.sub_type,"account")
		doc=frappe.new_doc("Journal Entry")
		acc=[{
			"account": account,
			"debit_in_account_currency":self.amount
		},
		{
			"account": "Buildings - MM",
			"credit_in_account_currency":self.amount
		}
		]
		doc.update({
			"company":"Money Manager",
			"voucher_type":"Journal Entry",
			"posting_date":date.today(),
			"accounts": acc
			})

		doc.insert()
		doc.submit()
		frappe.db.commit()
