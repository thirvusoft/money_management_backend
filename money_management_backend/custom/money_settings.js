frappe.ui.form.on('TS Money Management Settings', {
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
						frappe.set_route("user-permission")
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
						    frappe.set_route("user-permission")
							//frappe.set_route("ts-subtype",frm.doc.sub_type)

						
					}
				})
				 
			});
	},
	
	
})