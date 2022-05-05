frappe.ui.form.on('TS User Assign Setting', {
	type: function(frm) {
	frm.set_query("sub_type", function() {
		return {
			filters: {
				'ts_type': frm.doc.type
			}
		}
	});
},
	refresh: function(frm) {

			cur_frm.add_custom_button(__('Assign '),function(){
				frappe.call({
					method:"money_management_backend.custom.money_settings.add_user",
					args:{
						'user':cur_frm.doc.user,
						'subtype':cur_frm.doc.sub_type
					},
					callback: function(r){
						frappe.msgprint(__(" {0} - User Assigned for {1} Subtype",[cur_frm.doc.user ,  r.message]));
					}
				})

			});
			cur_frm.add_custom_button(__('Remove '),function(){
				frappe.call({
					method:"money_management_backend.custom.money_settings.terminate_user",
					args:{
						'user':cur_frm.doc.user,
						'subtype':cur_frm.doc.sub_type
					},
					callback: function(r){
						     
						    frappe.msgprint(__(" {0} - User Permission Removed for {2} Subtype",[cur_frm.doc.user , cur_frm.doc.sub_type, r.message]));
						    //frappe.set_route("user-permission")
							//frappe.set_route("ts-subtype",frm.doc.sub_type)

						
					}
				})
				 
			});
			frm.disable_save();
	},
	
	
	
})