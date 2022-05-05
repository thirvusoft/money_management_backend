import frappe
from frappe.model.document import Document
from datetime import date

class AmountisZero(Exception):
	http_status_code = 417
	
class TSDailyEntrySheet(Document):
	def after_insert(self):
		if(self.type in ['Expense','Asset','Liability','Income']):
			if(not int(self.amount)):
				frappe.throw('Amount is Mandatory',AmountisZero)
			credit_account=frappe.db.get_single_value('TS Settings','account_to_credit')
			debit_account=frappe.db.get_single_value('TS Settings','account_to_debit')
			company=frappe.db.get_single_value('Global Defaults','default_company')
			account= frappe.get_value("TS Subtype", self.sub_type,"account")
			if(not account):
				frappe.throw(f'Account does not exist for {self.sub_type}.',frappe.DoesNotExistError)
			else:
				frappe.get_doc('Account',account)
				
			doc=frappe.new_doc("Journal Entry")
			if(self.type in ['Expense','Liability']):
				account = debit_account
			acc=[{
				"account": account,
				"debit_in_account_currency":self.amount
			},
			{
				"account": credit_account,
				"credit_in_account_currency":self.amount
			}]
			doc.update({
				"company":company,
				"voucher_type":"Journal Entry",
				"posting_date":date.today(),
				"accounts": acc
				})

			doc.insert()
			doc.submit()
			frappe.db.commit()