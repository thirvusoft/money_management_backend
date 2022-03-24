// Copyright (c) 2022, Thirvusoft and contributors
// For license information, please see license.txt


//Precious metal quality display based on metal
frappe.ui.form.on('TS Money Manager', {
	ts_asset_subtype: function(frm) {
		if (frm.doc.sub_type_name == "Gold")
			{
			cur_frm.set_df_property('ts_quality','options', [' ', '24 karat','22 karat', '20 Karat', '18 karat', '14 Karat', '10 Karat'])
		}
		else if (frm.doc.sub_type_name == "Silver")
		{
			frm.set_df_property('ts_quality', 'options', [ 'Fine Silver', 'Sterling Silver','Non-Tarnish Silver', 'Britannia Silver', 'Coin Silver', 'European Silver', 'Silver-Filled', 'Silver Plated', 'Tibetan Silver', 'Tribal Silver', 'Nickel Silver' ])
		}
		else if (frm.doc.sub_type_name == "Platinum")
		{
			frm.set_df_property('ts_quality', 'options', [ 'Eternal', 'Pure', 'Rare', 'Versatile' ])
		}
		else if (frm.doc.sub_type_name == "Diamond")
		{
			frm.set_df_property('ts_quality', 'options', [ 'Heavily Included', 'Included', 'Slightly Included', 'Very Slightly Included', 'Very Very Slightly Included', 'Internally Flawless', 'Flawless' ])
			
		}
	}
});

// To display the subtype match to entry type

frappe.ui.form.on('TS Money Manager', 
{
	ts_entry_type:function(frm)
	{
	    frm.set_query("ts_asset_subtype", function() {
           let entry=frm.doc.ts_entry_type;
            return {
                filters:
				[
                    ['ts_type','=',entry],
					['fromfe','=',0]
				]
            };
        });
	},
	ts_asset_subtype:function(frm)
	{	
	    if(frm.doc.ts_asset_subtype=="" || cur_frm.doc.ts_asset_subtype==null){
			cur_frm.set_value('sub_type_name','');
			cur_frm.set_df_property('sub_type_name','hidden',1);
		}
		else{
			cur_frm.set_df_property('sub_type_name','hidden',0);
		}
	},
	
})


//refresh the subtype while changing the entry type
//In Dept - subtype calculate the interest amount automatically

frappe.ui.form.on('TS Money Manager', {
	ts_entry_type:function(frm) {
		cur_frm.set_value("ts_asset_subtype", "")
	},
	ts_debt_credit_amount: function(frm) {
		frm.set_value("ts_interest_amount",flt((frm.doc.ts_debt_credit_amount)*flt(frm.doc.ts_interest_rate))/100);
	},
	  ts_interest_rate: function(frm) {
		frm.set_value("ts_interest_amount",flt((frm.doc.ts_debt_credit_amount)*flt(frm.doc.ts_interest_rate))/100);
	}
});


