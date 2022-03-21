// Copyright (c) 2016, saheeth and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["daily sheet Report"] = {
	"filters": [
		{
			"fieldname" :"ts_type",
			"label" : __("choose the Type"),
			"fieldtype" : "Select",
			"options" : ['Asset','Expense','Income','Liability','Others'],
			"default": frappe.defaults.get_user_default("Asset"),
			"reqd":1
		}

	]
};

