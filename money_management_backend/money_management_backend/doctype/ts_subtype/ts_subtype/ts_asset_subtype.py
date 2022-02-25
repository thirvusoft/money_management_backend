# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TSAssetSubtype(Document):
    pass
#     def uvalidate(self):
#         if(self.icon=="aa"):
#             subtype_list_dict=[{'ts_subentry_type': 'Asset', 'ts_subtype': 'Gold', 'icon': 'Icons.circle_notifications_outlined'}, {'ts_subentry_type': 'Asset', 'ts_subtype': 'Silver', 'icon': 'Icons.card_travel'}, {'ts_subentry_type': 'Asset', 'ts_subtype': 'Platinum', 'icon': 'Icons.add_alert_rounded'}, {'ts_subentry_type': 'Asset', 'ts_subtype': 'Vehicle', 'icon': 'Icons.car_repair'}, {'ts_subentry_type': 'Liability', 'ts_subtype': 'Debt', 'icon': 'Icons.account_balance'}, {'ts_subentry_type': 'Liability', 'ts_subtype': 'EMI', 'icon': 'Icons.account_balance'}, {'ts_subentry_type': 'Income', 'ts_subtype': 'Salary', 'icon': 'Icons.attach_money'}, {'ts_subentry_type': 'Income', 'ts_subtype': 'Asset', 'icon': 'Icons.money_sharp'}, {'ts_subentry_type': 'Income', 'ts_subtype': 'Scrap', 'icon': 'wb_shade_outlined'}, {'ts_subentry_type': 'Expense', 'ts_subtype': 'Food', 'icon': 'Icons.food_bank_outlined'}, {'ts_subentry_type': 'Expense', 'ts_subtype': 'Travel', 'icon': 'Icons.flight'}, {'ts_subentry_type': 'Expense', 'ts_subtype': 'Grocery', 'icon': 'Icons.badge'}, {'ts_subentry_type': 'Others', 'ts_subtype': 'Invitation', 'icon': 'Icons.indeterminate_check_box_outlined'}, {'ts_subentry_type': 'Others', 'ts_subtype': 'Profile', 'icon': 'Icons.portrait_sharp'}, {'ts_subentry_type': 'Others', 'ts_subtype': 'Visiting Card', 'icon': 'Icons.indeterminate_check_box_outlined'}]
#             for subtype in subtype_list_dict:
#                 st=frappe.new_doc("TS Asset Subtype")
#                 st.update(subtype)
#                 st.update({"doctype":"TS Asset Subtype"})
#                 st.save()