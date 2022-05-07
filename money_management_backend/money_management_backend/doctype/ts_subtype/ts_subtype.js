// Copyright (c) 2022, saheeth and contributors
// For license information, please see license.txt

frappe.ui.form.on('TS Subtype', {
	refresh: function(frm) {
		    let a =cur_frm.doc.ts_type
			cur_frm.set_value("link_type",a) 
		
			console.log(a)
			console.log(cur_frm.doc.link_type)
		
	     },
	link_type: function(frm) {
		frm.set_query("link_doc_subtype", function() {
			return {
				filters: {
					'ts_type': frm.doc.link_type,
					'fromfe':0
				}
			}
		});
	},

});
