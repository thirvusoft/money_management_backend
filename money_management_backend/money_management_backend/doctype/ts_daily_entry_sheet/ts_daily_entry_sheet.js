// Copyright (c) 2022, saheeth and contributors
// For license information, please see license.txt

frappe.ui.form.on('TS Daily Entry Sheet',
 {
	type :function(frm)
	{
		frm.set_query("sub_type", function(){
<<<<<<< HEAD
			let custom=frm.doc.type;
			return{
				filters:
				[
					['ts_type', '=',custom]
=======
			let type=frm.doc.type;
			return{
				filters:
				[
					['ts_type', '=',type],
					['fromfe', '=',1]
>>>>>>> 02dba95e76fa204daf39298b226935dca4d160e2
				]
			};
		});                             
	}
});




