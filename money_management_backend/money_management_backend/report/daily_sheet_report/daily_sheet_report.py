# Copyright (c) 2013, saheeth and contributors
# For license information, please see license.txt

import frappe

from multiprocessing import Condition
import frappe
from frappe.utils import data
def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_columns(filters):
        #"depends_on":'eval:in_list(["Liability"], doc.ts_type)'
            # "depends_on":'eval:doc.ts_type=="Property"',
    #"options":['Gold','Silver','Platinum','Diamond','Vehicle','Home Appliances','Machinery','Agri Land','Commercial Land','Residential'],
    columns = [
        {
            "label": ("Sub type"),
            "fieldtype": "Data",
            "fieldname": "sub_type",
            "width": 130
        },

        {
            "label": ("Name"),
            "fieldtype":"Data",
            "fieldname": "entry_name",
            "width": 130
        },
        {
            "label": ("Amount"),
            "fieldtype":"Currency",
            "fieldname": "amount",
            "width": 130
            }
            ]
    if filters['ts_type'] == 'Liability':
        columns += [{
            
                "label": ("Remainder Date"),
                "fieldtype":"Date",
                "fieldname": "remainder_date",
                "width": 130 ,
                
            }]

    return columns
    
def get_conditions(filters):
    conditions = {}
    if filters.ts_type:
        conditions["type"] = filters.ts_type
    return conditions

# def get_data(filters):
# 	conditions = {"ts_type":filters['ts_type']}
# 	fields = []
# 	if 'Asset' in filters:
# 		conditions['ts_type'] = filters['ts_type']
# 		if filters['ts_type'] == 'Asset':
# 			fields =['sub_type','entry_name','amount']
# 		if fields:
# 			data1=frappe.get_all('TS Daily Entry Sheet',conditions,fields)
# 			return data1
# 		return []

def get_data(filters):
    data = []
    conditions = get_conditions(filters)
    if filters.ts_type =='Asset':

        docs = frappe.db.get_all("TS Daily Entry Sheet", conditions, ["sub_type","entry_name","amount"])
        print(docs)
        for d in docs:
            row = {"sub_type": d.sub_type, "entry_name": d.entry_name,"amount":d.amount}
            data.append(row)
        #return data
    if filters.ts_type =='Liability':

        docs = frappe.db.get_all("TS Daily Entry Sheet", conditions, ["sub_type","entry_name","amount","remainder_date"])
        print(docs)
        for d in docs:
            row = {"sub_type": d.sub_type, "entry_name": d.entry_name,"amount":d.amount,"remainder_date":d.remainder_date}
            data.append(row)
        # return data

    if filters.ts_type =='Expense':

        docs = frappe.db.get_all("TS Daily Entry Sheet", conditions, ["sub_type","entry_name","amount"])
        print(docs)
        for d in docs:
            row = {"sub_type": d.sub_type, "entry_name": d.entry_name,"amount":d.amount}
            data.append(row)
        # return data
    
    if filters.ts_type =='Income':

        docs = frappe.db.get_all("TS Daily Entry Sheet", conditions, ["sub_type","entry_name","amount"])
        print(docs)
        for d in docs:
            row = {"sub_type": d.sub_type, "entry_name": d.entry_name,"amount":d.amount}
            data.append(row)
        # return data

    if filters.ts_type =='Others':

        docs = frappe.db.get_all("TS Daily Entry Sheet", conditions, ["sub_type","entry_name","amount"])
        print(docs)
        for d in docs:
            row = {"sub_type": d.sub_type, "entry_name": d.entry_name,"amount":d.amount}
            data.append(row)
    return data
	


