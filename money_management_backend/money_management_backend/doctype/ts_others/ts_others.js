
// For license information, please see license.txt

let others=""
frappe.ui.form.on('TS Others', {
entry_type: function(frm,cdt,cdn)
{
	let other=locals[cdt][cdn]
	if(others!=other.entry_type){
		others=other.entry_type
		frappe.model.set_value(cdt, cdn, "notes")
		frappe.model.set_value(cdt, cdn, "file_upload")
		cur_frm.refresh_fields();
		}
	 }
});

frappe.ui.form.on('TS Others', 
{
	onload:function(frm)
	
	{
	    frm.set_query("entry_type", function() {

            return {
                filters:
				[
                    ['ts_type','=',"Others"],
					['flutter','=',"0"]
                ]
            };
        });
	}
});