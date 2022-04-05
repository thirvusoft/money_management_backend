// Copyright (c) 2022, saheeth and contributors
// For license information, please see license.txt

frappe.ui.form.on('TS Settings', {
	setup:function(frm){
	frm.set_query('parent_acc',function(){
		return {
			filters:{
				'is_group':1,
				'parent_account':''
			}
		}
	})
	}
});
