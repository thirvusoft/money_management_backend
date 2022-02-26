// Copyright (c) 2022, Thirvusoft and contributors
// For license information, please see license.txt



frappe.ui.form.on('TS Money Manager', {
	ts_asset_subtype: function(frm) {
		if (frm.doc.ts_asset_subtype == "Gold")
			{
			frm.set_df_property('ts_quality','options', [' ', '24 karat','22 karat', '20 Karat', '18 karat', '14 Karat', '10 Karat'])
		}
		else if (frm.doc.ts_asset_subtype == "Silver")
		{
			frm.set_df_property('ts_quality', 'options', [ 'Fine Silver', 'Sterling Silver','Non-Tarnish Silver', 'Britannia Silver', 'Coin Silver', 'European Silver', 'Silver-Filled', 'Silver Plated', 'Tibetan Silver', 'Tribal Silver', 'Nickel Silver' ])
		}
		else if (frm.doc.ts_asset_subtype == "Platinum")
		{
			frm.set_df_property('ts_quality', 'options', [ 'Eternal', 'Pure', 'Rare', 'Versatile' ])
		}
		else if (frm.doc.ts_asset_subtype == "Diamond")
		{
			frm.set_df_property('ts_quality', 'options', [ 'Heavily Included', 'Included', 'Slightly Included', 'Very Slightly Included', 'Very Very Slightly Included', 'Internally Flawless', 'Flawless' ])
			
		}
	}
});



frappe.ui.form.on('TS Money Manager', {
	ts_entry_type:function(frm) {
	    frm.set_query("ts_asset_subtype", function() {
           let entry=frm.doc.ts_entry_type;
            return {
                filters: [
                    ['ts_subentry_type','=',entry]
                ]
            };
        });
	}
})

