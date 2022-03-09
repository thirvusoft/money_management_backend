

frappe.ui.form.on('TS Expense', 
{
	onload:function(frm)
	
	{
	    frm.set_query("subtype", function() {

            return {
                filters:
				[
                    ['ts_type','=',"Expense"],
					['flutter','=',"0"]
                ]
            };
        });
	}
});

let home=""
let maintain=""
let insure=""
frappe.ui.form.on('TS Expense', 
{ 
	home_need_type: function(frm,cdt,cdn)
	{
		let home_need=locals[cdt][cdn]
		if(home!==home_need.home_need_type){
			home=home_need.home_need_type
		frappe.model.set_value(cdt,cdn, "shopping_date", "")
		frappe.model.set_value(cdt,cdn, "gshop_name", "")
		frappe.model.set_value(cdt,cdn, "hmobile_number", "")
		frappe.model.set_value(cdt,cdn, "location", "")
		frappe.model.set_value(cdt,cdn, "amount", "")
		frappe.model.set_value(cdt,cdn, "notes", "")
		cur_frm.clear_table("expense_bill_documents");
		cur_frm.clear_table("grocery_item_list");
		cur_frm.refresh_fields();

	}
	},
	
	maintenance_to: function(frm,cdt,cdn)
	{
		let maintenance=locals[cdt][cdn]
		if(maintain!==maintenance.maintenance_to){
		maintain=maintenance.maintenance_to
		frappe.model.set_value(cdt,cdn, "maintenance_type", "")
		frappe.model.set_value(cdt,cdn, "cost", "")
	}	
	},

	insurance_type: function(frm,cdt,cdn)
	{
		let insurance=locals[cdt][cdn]
		if(insure!==insurance.insurance_type){
			insure=insurance.insurance_type
			frappe.model.set_value(cdt,cdn, "insured_company","")
			frappe.model.set_value(cdt,cdn, "insured_amount", "")
			frappe.model.set_value(cdt,cdn, "company_address", "")
			frappe.model.set_value(cdt,cdn, "notes", "")
			cur_frm.clear_table("insurance_document")
			cur_frm.clear_table("iimage")
			cur_frm.refresh_fields();
		}
	},
	travel_expense_amount : function(frm) {
		frm.set_value("total_amount",flt(frm.doc.travel_expense_amount)+flt(frm.doc.food_expense_amount)+flt(frm.doc.other_expense_amount));
	},
		food_expense_amount: function(frm) {
		frm.set_value("total_amount",flt(frm.doc.travel_expense_amount)+flt(frm.doc.food_expense_amount)+flt(frm.doc.other_expense_amount));
	},
	other_expense_amount: function(frm) {
		frm.set_value("total_amount",flt(frm.doc.travel_expense_amount)+flt(frm.doc.food_expense_amount)+flt(frm.doc.other_expense_amount));
	  
	}
});
