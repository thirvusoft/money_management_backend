import frappe
def createdocs():

   subtype_list_dict= [{'ts_type': 'Asset', 'ts_subtype': 'Gold', 'icon_code': '0xf1dd', 'fromfe': '1', 'account': 'Gold - MM'}, {'ts_type': 'Asset', 'ts_subtype': 'Silver', 'icon_code': '0xf1dd', 'fromfe': '1', 'account': 'Silver - MM'}, {'ts_type': 'Asset', 'ts_subtype': 'Platinum', 'icon_code': '0xf1dd', 'fromfe': '1', 'account': 'Platinum - MM'}, {'ts_type': 'Asset', 'ts_subtype': 'Diamond', 'icon_code': '0xf05e7', 'fromfe': '1', 'account': 'Diamond - MM'}, {'ts_type': 'Asset', 'ts_subtype': 'Vehicles', 'icon_code': '0xee62', 'fromfe': '1', 'account': 'Vehicles - MM'}, {'ts_type': 'Asset', 'ts_subtype': 'Machinery', 'icon_code': '0xef06', 'fromfe': '1', 'account': 'Machinery - MM'}, {'ts_type': 'Asset', 'ts_subtype': 'Agri Land', 'icon_code': 'F104F', 'fromfe': '1', 'account': 'Agri Land - MM'}, {'ts_type': 'Asset', 'ts_subtype': 'Commercial', 'icon_code': '0xf42b', 'fromfe': '1', 'account': 'Commercial Land - MM'}, {'ts_type': 'Asset', 'ts_subtype': 'Estate', 'icon_code': '0xf1af', 'fromfe': '1', 'account': 'Estate - MM'}, {'ts_type': 'Asset', 'ts_subtype': '', 'icon_code': '0xf1dd', 'fromfe': '1'}, {'ts_type': 'Asset', 'ts_subtype': '', 'icon_code': '0xee62', 'fromfe': '1'}, {'ts_type': 'Asset', 'ts_subtype': '', 'icon_code': '0xf447', 'fromfe': '1'}, {'ts_type': 'Asset', 'ts_subtype': '', 'icon_code': '0xef06', 'fromfe': '1'}, {'ts_type': 'Asset', 'ts_subtype': '', 'icon_code': '0xf05ce', 'fromfe': '1'}, {'ts_type': 'Asset', 'ts_subtype': '', 'icon_code': '0xf42b', 'fromfe': '1'}, {'ts_type': 'Asset', 'ts_subtype': '', 'icon_code': '0xf1af', 'fromfe': '1'}, {'ts_type': 'Asset', 'ts_subtype': '', 'icon_code': '0xf447', 'fromfe': '1'}, {'ts_type': 'Asset', 'ts_subtype': '', 'icon_code': '0xf18e', 'fromfe': '1'}, {'ts_type': 'Asset', 'ts_subtype': '', 'icon_code': '0xee35', 'fromfe': '1'}, {'ts_type': 'Asset', 'ts_subtype': '', 'icon_code': '0xf2e9', 'fromfe': '1'}, {'ts_type': 'Asset', 'ts_subtype': '', 'icon_code': '0xf108', 'fromfe': '1'}, {'ts_type': 'Asset', 'ts_subtype': '', 'icon_code': '0xf05ce', 'fromfe': '1'}, {'ts_type': 'Asset', 'ts_subtype': 'Gold', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Asset', 'ts_subtype': 'Silver', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Asset', 'ts_subtype': 'Platinum', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Asset', 'ts_subtype': 'Diamond', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Asset', 'ts_subtype': 'Vehicle', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Asset', 'ts_subtype': 'Home Appliance', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Asset', 'ts_subtype': 'Machinery', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Asset', 'ts_subtype': 'Agricultural Land', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Asset', 'ts_subtype': 'Residential Land', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Asset', 'ts_subtype': 'Commercial Land', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Liability', 'ts_subtype': 'Debt', 'icon_code': '0xeea2', 'fromfe': '1', 'account': 'Debt - MM'}, {'ts_type': 'Liability', 'ts_subtype': 'EMI', 'icon_code': '0xf2d1', 'fromfe': '1', 'account': 'EMI - MM'}, {'ts_type': 'Liability', 'ts_subtype': '', 'icon_code': '0xeea2', 'fromfe': '1'}, {'ts_type': 'Liability', 'ts_subtype': '', 'icon_code': '0xf2d1', 'fromfe': '1'}, {'ts_type': 'Liability', 'ts_subtype': '', 'icon_code': '0xe13c', 'fromfe': '1'}, {'ts_type': 'Liability', 'ts_subtype': '', 'icon_code': '0xf0de', 'fromfe': '1'}, {'ts_type': 'Liability', 'ts_subtype': '', 'icon_code': '0xf05ff', 'fromfe': '1'}, {'ts_type': 'Liability', 'ts_subtype': 'Debt', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Liability', 'ts_subtype': 'EMI', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Income', 'ts_subtype': 'Salary', 'icon_code': '0xf04e1', 'fromfe': '1', 'account': 'Salary - MM'}, {'ts_type': 'Income', 'ts_subtype': 'Asset Sale', 'icon_code': '0xf2ee', 'fromfe': '1', 'account': 'Asset Sale - MM'}, {'ts_type': 'Income', 'ts_subtype': 'Scrap Sale', 'icon_code': '0xf18e', 'fromfe': '1', 'account': 'Scrap Scale - MM'}, {'ts_type': 'Income', 'ts_subtype': 'Rental', 'icon_code': '0xf244', 'fromfe': '1', 'account': 'Rental - MM'}, {'ts_type': 'Income', 'ts_subtype': 'Refunds', 'icon_code': '0xf2d6', 'fromfe': '1', 'account': 'Refunds - MM'}, {'ts_type': 'Income', 'ts_subtype': 'Coupons', 'icon_code': '0xf3f6', 'fromfe': '1', 'account': 'Coupons - MM'}, {'ts_type': 'Income', 'ts_subtype': 'Lottery', 'icon_code': '0xf3e8', 'fromfe': '1', 'account': 'Lottery - MM'}, {'ts_type': 'Income', 'ts_subtype': 'Dividend', 'icon_code': '0xf0617', 'fromfe': '1', 'account': 'Dividend - MM'}, {'ts_type': 'Income', 'ts_subtype': 'Revenue', 'icon_code': '0xee35', 'fromfe': '1', 'account': 'Revenue - MM'}, {'ts_type': 'Income', 'ts_subtype': '', 'icon_code': '0xf04e1', 'fromfe': '1'}, {'ts_type': 'Income', 'ts_subtype': '', 'icon_code': '0xf2ee', 'fromfe': '1'}, {'ts_type': 'Income', 'ts_subtype': '', 'icon_code': '0xf18e', 'fromfe': '1'}, {'ts_type': 'Income', 'ts_subtype': '', 'icon_code': '0xf244', 'fromfe': '1'}, {'ts_type': 'Income', 'ts_subtype': '', 'icon_code': '0xf2d6', 'fromfe': '1'}, {'ts_type': 'Income', 'ts_subtype': '', 'icon_code': '0xf3f6', 'fromfe': '1'}, {'ts_type': 'Income', 'ts_subtype': '', 'icon_code': '0xf3e8', 'fromfe': '1'}, {'ts_type': 'Income', 'ts_subtype': '', 'icon_code': '0xf0617', 'fromfe': '1'}, {'ts_type': 'Income', 'ts_subtype': '', 'icon_code': '0xee35', 'fromfe': '1'}, {'ts_type': 'Income', 'ts_subtype': 'Salary', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Income', 'ts_subtype': 'Asset/Scrap Sale', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Income', 'ts_subtype': 'Rental', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Income', 'ts_subtype': 'Lottery', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Income', 'ts_subtype': 'Dividends', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Income', 'ts_subtype': 'Business Profit', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Expense', 'ts_subtype': 'Food', 'icon_code': '0xf2e9', 'fromfe': '1', 'account': 'Food - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Travel', 'icon_code': '0xf172', 'fromfe': '1', 'account': 'Travel - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Grocery', 'icon_code': '0xf37d', 'fromfe': '1', 'account': 'Grocery - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Fun', 'icon_code': '0xf3cf', 'fromfe': '1', 'account': 'Fun - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Shopping', 'icon_code': '0xf37f', 'fromfe': '1', 'account': 'Shopping - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Insurance', 'icon_code': '0xf05f0', 'fromfe': '1', 'account': 'Insurance - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Tax', 'icon_code': '0xf24e', 'fromfe': '1', 'account': 'Tax - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Gas', 'icon_code': '0xf076', 'fromfe': '1', 'account': 'Gas - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Power', 'icon_code': '0xf016', 'fromfe': '1', 'account': 'Power - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Telephone', 'icon_code': '0xf28c', 'fromfe': '1', 'account': 'Telephone - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Mobile', 'icon_code': '0xf28d', 'fromfe': '1', 'account': 'Mobile - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Health', 'icon_code': '0xf0f2', 'fromfe': '1', 'account': 'Health - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Beauty', 'icon_code': '0xf041', 'fromfe': '1', 'account': 'Beauty - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Electronic', 'icon_code': '0xef0d', 'fromfe': '1', 'account': 'Electronic - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Gift', 'icon_code': '0xef2d', 'fromfe': '1', 'account': 'Gift - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Education', 'icon_code': '0xf33c', 'fromfe': '1', 'account': 'Education - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Maintain', 'icon_code': '0xf108', 'fromfe': '1', 'account': 'Maintain - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Social', 'icon_code': '0xf06a4', 'fromfe': '1', 'account': 'Social - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Building', 'icon_code': '0xf109', 'fromfe': '1', 'account': 'Building - MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Crop', 'icon_code': '0xf05ce', 'fromfe': '1', 'account': 'Crop -MM'}, {'ts_type': 'Expense', 'ts_subtype': 'Fertilizer', 'icon_code': '0xf068b', 'fromfe': '1', 'account': 'Fertilizer - MM'}, {'ts_type': 'Expense', 'ts_subtype': '', 'icon_code': '0xf2e9', 'fromfe': '1'}, {'ts_type': 'Expense', 'ts_subtype': '', 'icon_code': '0xf172', 'fromfe': '1'}, {'ts_type': 'Expense', 'ts_subtype': '', 'icon_code': '0xf37d', 'fromfe': '1'}, {'ts_type': 'Expense', 'ts_subtype': '', 'icon_code': '0xf3cf', 'fromfe': '1'}, {'ts_type': 'Expense', 'ts_subtype': '', 'icon_code': '0xf3cf', 'fromfe': '1'}, {'ts_type': 'Expense', 'ts_subtype': 'Home Need', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Expense', 'ts_subtype': 'Travel', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Expense', 'ts_subtype': 'Insurance', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Expense', 'ts_subtype': 'Tax', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Expense', 'ts_subtype': 'Gift', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Expense', 'ts_subtype': 'Education', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Expense', 'ts_subtype': 'Social Service', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Expense', 'ts_subtype': 'Maintenance', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Expense', 'ts_subtype': 'Construction', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Expense', 'ts_subtype': 'Agriculture', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Others', 'ts_subtype': 'Invite', 'icon_code': '0xf12f', 'fromfe': '1', 'account': 'Invite - MM'}, {'ts_type': 'Others', 'ts_subtype': 'Profile', 'icon_code': '0xee35', 'fromfe': '1', 'account': 'Profile -MM'}, {'ts_type': 'Others', 'ts_subtype': 'Call Card', 'icon_code': '0xef8f', 'fromfe': '1', 'account': 'Call Card - MM'}, {'ts_type': 'Others', 'ts_subtype': 'Credit Card', 'icon_code': '0xef8f', 'fromfe': '1', 'account': 'Credit card - MM'}, {'ts_type': 'Others', 'ts_subtype': 'Gifts', 'icon_code': '0xef2d', 'fromfe': '1', 'account': 'Gifts - MM'}, {'ts_type': 'Others', 'ts_subtype': 'wallet', 'icon_code': '0xee33', 'fromfe': '1', 'account': 'Wallet - MM'}, {'ts_type': 'Others', 'ts_subtype': 'Message', 'icon_code': '0xf2dd', 'fromfe': '1', 'account': 'Message - MM'}, {'ts_type': 'Others', 'ts_subtype': '', 'icon_code': '0xf197', 'fromfe': '1'}, {'ts_type': 'Others', 'ts_subtype': '', 'icon_code': '0xf128', 'fromfe': '1'}, {'ts_type': 'Others', 'ts_subtype': '', 'icon_code': '0xf440', 'fromfe': '1'}, {'ts_type': 'Others', 'ts_subtype': '', 'icon_code': '0xf14f', 'fromfe': '1'}, {'ts_type': 'Others', 'ts_subtype': 'Invitation', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Others', 'ts_subtype': 'Profile', 'icon_code': '', 'fromfe': '0'}, {'ts_type': 'Others', 'ts_subtype': 'Visiting Card', 'icon_code': '', 'fromfe': '0'}]

   for subtype in subtype_list_dict:
       st=frappe.new_doc("TS Subtype")
       st.update(subtype)
       st.update({"doctype":"TS Subtype"})
       st.save()