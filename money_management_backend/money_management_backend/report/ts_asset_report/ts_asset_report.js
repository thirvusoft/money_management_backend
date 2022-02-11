// Copyright (c) 2016, saheeth and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["TS Asset Report"] = {
	"filters": [
		{
			"fieldname" :"ts_asset_type",
			"label" : __("Select Asset Type"),
			"fieldtype" : "Select",
			"reqd":1,
			"options" : ['Movable','Property'],
		},
		{
			"fieldname" :"ts_movable_type",
			"label" : __("Select Movable Type"),
			"fieldtype" : "Link",
			"options" : "TS Movable List",
			"default": frappe.defaults.get_user_default("Select Movable Type"),
			depends_on:'eval:doc.ts_asset_type=="Movable"'
		},
	
		{
			"fieldname" :"ts_property_type",
			"label" : __("Property Type"),
			"fieldtype" : "Link",
			"options" : "TS Property",
			"default": frappe.defaults.get_user_default("Property Type"),
			depends_on:'eval:doc.ts_asset_type=="Property"'
		}
	]

};
