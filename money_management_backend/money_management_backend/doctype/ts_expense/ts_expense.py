# Copyright (c) 2022, saheeth and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe import _
from frappe.model.document import Document
from datetime import date

class AmountisZero(Exception):
    http_status_code = 417

class TSExpense(Document):
	def validate(doc):
		if doc.subtype_name == "Social Service":
			aadhar=doc.ts_aadhar_number
			if aadhar or aadhar==0:
				if not aadhar.isdigit() or len(aadhar) != 12:
					frappe.throw(frappe._("Invalid Aadhar Number. {0} is not 16 digit.").format(aadhar), frappe.InvalidPhoneNumberError)
		elif doc.subtype_name == "Gift":
			gift_aadhar=doc.ts_aadhar_no
			if gift_aadhar or gift_aadhar==0:
				if not gift_aadhar.isdigit() or len(gift_aadhar) != 12:
					frappe.throw(frappe._("Invalid Aadhar Number. {0} is not 16 digit.").format(gift_aadhar), frappe.InvalidPhoneNumberError)
		elif doc.subtype_name != ["Agriculture","Construction","Maintenance","SocialService","Education","Gift","Tax","Insurance","Travel","Home Need","Building","Social Service","Maintanance"]:
			aadhar_no=doc.ts_aadhar_number1
			if aadhar_no or aadhar_no==0:
				if not aadhar_no.isdigit() or len(aadhar_no) != 12:
					frappe.throw(frappe._("Invalid Aadhar Number. {0} is not 16 digit.").format(aadhar_no), frappe.InvalidPhoneNumberError)
		else :
			pass

	def after_insert(self):
		total_amount = {"Home Need":"amount","Travel":"total_amount","Insurance":"insured_amount","Tax":"tax_amount","Gift":"gamount","Education":"iamount","Social Service":"oamount","Maintenance":"cost","Construction":"ts_expense_bill_amount"}
		try:
			amount = eval("self."+total_amount[self.subtype_name])
		except:
			try:
				amount = self.yeild_expense
			except:
				try:
					amount = self.fertilizer_expense
				except:
					amount = self.ts_amount
		if(not int(amount)):
			frappe.throw('Amount is Mandatory',AmountisZero)
		debit_account=frappe.db.get_single_value('Thirvu Settings','account_to_debit')
		company=frappe.db.get_single_value('Global Defaults','default_company')
		account= frappe.get_value("TS Subtype", self.subtype,"account")
		if(not account):
			frappe.throw(f'Account does not exist for {self.subtype}.',frappe.DoesNotExistError)
		else:
			frappe.get_doc('Account',account)
		doc=frappe.new_doc("Journal Entry")
		acc=[{
			"account": account,
			"credit_in_account_currency":amount
		},
		{
			"account": debit_account,
			"debit_in_account_currency":amount
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