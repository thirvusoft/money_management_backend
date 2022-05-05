# Copyright (c) 2022, Thirvusoft and contributors
# For license information, please see license.txt

from ast import Pass
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from datetime import date


class AmountisZero(Exception):
	http_status_code = 417

class TSMoneyManager(Document):
	def validate(self):
		asset=["Vehicle", "Home Appliance", "Machinery", "Agricultural Land", "Commercial Land", "Residential Land"]
		if(self.sub_type_name=='Debt'):
			selleradhar=self.ts_creditor_aadhar_number
			if selleradhar or selleradhar==0:
				if not selleradhar.isdigit() or len(selleradhar) != 12:
					frappe.throw(frappe._("{0} is more or less then 12 digit. Enter a valid Aadhar Number.").format(selleradhar), frappe.InvalidPhoneNumberError)
		elif self.sub_type_name in asset:
			selleradhar=self.ts_seller_aadhar
			if selleradhar or selleradhar==0:
				if not selleradhar.isdigit() or len(selleradhar) != 12:
					frappe.throw(frappe._("{0} is more or less then 12 digit. Enter a valid Aadhar Number.").format(selleradhar), frappe.InvalidPhoneNumberError)
		elif (self.sub_type_name =="Rental"):
			selleradhar=self.ts_raadhar_number
			if selleradhar or selleradhar==0:
				if not selleradhar.isdigit() or len(selleradhar) != 12:
					frappe.throw(frappe._("{0} is more or less then 12 digit. Enter a valid Aadhar Number.").format(selleradhar), frappe.InvalidPhoneNumberError)
		elif (self.sub_type_name =="Asset/Scrap Sale"):
			selleradhar=self.ts_saadhar
			if selleradhar or selleradhar==0:
				if not selleradhar.isdigit() or len(selleradhar) != 12:
					frappe.throw(frappe._("{0} is more or less then 12 digit. Enter a valid Aadhar Number.").format(selleradhar), frappe.InvalidPhoneNumberError)
		elif self.sub_type_name == "Interest Collection":
			interest_aadhar=self.ts_iaadhar_no
			if interest_aadhar or interest_aadhar==0:
				if not interest_aadhar.isdigit() or len(interest_aadhar) != 12:
					frappe.throw(frappe._("Invalid Aadhar Number. {0} is not 12 digit.").format(interest_aadhar), frappe.InvalidPhoneNumberError)
		elif self.sub_type_name != ["Business Profit","Dividends","Lottery","Rental","Asset/Scrap Sale","Salary","Revenue","Dividend","Lottery","Coupons","Refunds","Rental","Scrap Sale","Asset Sale","Salary","Commercial Land","Residential Land","Agricultural Land","Machinery","Home Appliance","Vehicle","Diamond","Platinum","Silver","Gold", "EMI","Debt"]:
			aadhar_no=self.ts_aadhar_number
			if aadhar_no or aadhar_no==0:
				if not aadhar_no.isdigit() or len(aadhar_no) != 12:
					frappe.throw(frappe._("Invalid Aadhar Number. {0} is not 12 digit.").format(aadhar_no), frappe.InvalidPhoneNumberError)
		else:
			Pass

	def autoname(doc):
		if doc.ts_entry_type == "Income": 
			doc.name = make_autoname(doc.ts_entry_type + ".####")
		elif doc.ts_entry_type == "Asset": 
			doc.name = make_autoname(doc.ts_entry_type + ".####")
		elif doc.ts_entry_type == "Liability": 
			doc.name = make_autoname(doc.ts_entry_type + ".####")

	def after_insert(self):
		if(self.sub_type_name in ["Gold","Silver","Platinum","Diamond","Vehicle","Home Appliance","Machinery","Agricultural Land","Residential Land","Commercial Land"]):
			amount = self.ts_purchase_rate or 0
		else:
			try:
				total_amount = {"Crypto Currency":"ts_amount","Debt":"ts_debt_credit_amount","EMI":"ts_emi_amount","Salary":"ts_salary_amount","Crypto":"ts_amount",
				"Interest Collection":"ts_interestamount","Asset/Scrap Sale":"ts_sold_price","Rental":"ts_rental_amount","Lottery":"ts_lottery_amount",
				"Dividends":"ts_share_amount","Business Profit":"ts_bprofit_amount"}
				amount = eval("self."+total_amount[self.sub_type_name])
			except:
				amount = self.ts_amount1 or 0
		if(not int(amount)):
			frappe.throw('Amount is Mandatory',AmountisZero)
		credit_account=frappe.db.get_single_value('Thirvu Settings','account_to_credit')
		debit_account=frappe.db.get_single_value('Thirvu Settings','account_to_debit')
		company=frappe.db.get_single_value('Global Defaults','default_company')
		account= frappe.get_value("TS Subtype", self.ts_asset_subtype,"account")
		if(not account):
			frappe.throw(f'Account does not exist for {self.ts_asset_subtype}.',frappe.DoesNotExistError)
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