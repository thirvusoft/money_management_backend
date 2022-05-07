frappe.ui.form.on('TS User Assign Setting', {
	type: function(frm) {
	frm.set_query("sub_type", function() {
		return {
			filters: {
				'ts_type': frm.doc.type,
				'fromfe':1
			}
		}
	});
},
	type:function(frm)
	{	
	    if(frm.doc.type==""){
			cur_frm.set_value('sub_type','');
			cur_frm.set_df_property('sub_type');
		}
		else{
			cur_frm.set_value('sub_type','')
			frm.set_query("sub_type", function() {
				return {
					filters: {
						'ts_type': frm.doc.type,
						'fromfe':1
					}
				}
			});
		}
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

frappe.ui.form.on('TS User Assign Setting', {
	refresh: function(frm) {
		    let a = ''
			cur_frm.set_value("user",a) 
			cur_frm.set_value("type",a) 
			cur_frm.set_value("sub_type",a) 
	     },	
})
