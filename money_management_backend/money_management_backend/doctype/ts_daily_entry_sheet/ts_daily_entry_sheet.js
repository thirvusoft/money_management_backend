// Copyright (c) 2022, saheeth and contributors
// For license information, please see license.txt

frappe.ui.form.on('TS Daily Entry Sheet',
 {
	type :function(frm)
	{
		frm.set_query("sub_type", function(){
			let custom=frm.doc.type;
			return{
				filters:
				[
					['ts_type', '=',custom]
				]
			};
		});                             
	}
});




