 
 
fields=["ts_type","ts_subtype","icon_code" ,"fromfe","account"]
Asset=[
      ["Gold","0xf1dd","1","Gold - MM"],
      ["Silver","0xf1dd","1","Silver - MM"],
      ["Platinum","0xf1dd","1","Platinum - MM"],
      ["Diamond","0xf05e7","1","Diamond - MM"],
      ["Vehicles","0xee62","1","Vehicles - MM"],
      ["Home Appliance","0xf447","1","Home Applience - MM"],
      ["Machinery","0xef06","1","Machinery - MM"],
      ["Agri Land","F104F","1","Agri Land"],
      ["Commercial Land","0xf42b","1","Commercial Land - MM"],
      ["Residential Land","0xf1af","1","Residential Land - MM"],
      ["","0xf1dd","1"],
      ["","0xee62","1"],
      ["","0xf447","1"],
      ["","0xef06","1"],
      ["","0xf05ce","1"],
      ["","0xf42b","1"],
      ["","0xf1af","1"],
      ["","0xf447","1"],
      ["","0xf18e","1"],
      ["","0xee35","1"],
      ["","0xf2e9","1"],
      ["","0xf108","1"],
      ["","0xf05ce","1"]
 
   ]
Liability=[
   ["Debt","0xeea2","1","Debt - MM"],
   ["EMI","0xf2d1","1","EMI - MM"],
   ["","0xeea2","1"],
   ["","0xf2d1","1"],
   ["","0xe13c","1"],
   ["","0xf0de","1"],
   ["","0xf05ff","1"]
 
]
Income=[
  ["Salary","0xf04e1","1","Salary - MM"],
  ["Asset Sale","0xf2ee","1","Asset Sale - MM"],
  ["Scrap Sale","0xf18e","1","Scrap Scale - MM"],
  ["Rental","0xf244","1","Rental - MM"],
  ["Refunds","0xf2d6","1","Refunds - MM"],
  ["Coupons","0xf3f6","1","Coupons - MM"],
  ["Lottery","0xf3e8","1","Lottery - MM"],
  ["Dividends","0xf0617","1","Dividends - MM"],
  ["Business Profit","0xee35","1","Business Profit - MM"],
  ["","0xf04e1","1"],
  ["","0xf2ee","1"],
  ["","0xf18e","1"],
  ["","0xf244","1"],
  ["","0xf2d6","1"],
  ["","0xf3f6","1"],
  ["","0xf3e8","1"],
  ["","0xf0617","1"],
  ["","0xee35","1"]
]
 
Expense=[
  ["Food","0xf2e9","1","Food - MM"],
  ["Travel","0xf172","1","Travel - MM"],
  ["Grocery","0xf37d","1","Grocery - MM"],
  ["Entertainment","0xf3cf","1","Entertainment - MM"],
  ["Shopping","0xf37f","1","Shoping - MM"],
  ["Insurance","0xf05f0","1","Insurance - MM"],
  ["Tax","0xf24e","1","Tax - MM"],
  ["Gas","0xf076","1","Gas - MM"],
  ["Electricity","0xf016","1","Electricity - MM"],
  ["Telephone","0xf28c","1","Telephone - MM"],
  ["Mobile Recharge","0xf28d","1","Mobile Recharge - MM"],
  ["Health","0xf0f2","1","Health - MM"],
  ["Beauty","0xf041","1","Beauty - MM"],
  ["Electronics","0xef0d","1","Electricity - MM"],
  ["Gift","0xef2d","1","Gift - MM"],
  ["Education","0xf33c","1","Education - MM"],
  ["Maintenance","0xf108","1","Maintanence - MM"],
  ["Social Service","0xf06a4","1","Social Service - MM"],
  ["Construction","0xf109","1","Construction - MM"],
  ["Crop","0xf05ce","1","Crop -MM"],
  ["Fertilizer","0xf068b","1","Fertilizer - MM"],
  ["","0xf2e9","1"],
  ["","0xf172","1"],
  ["","0xf37d","1"],
  ["","0xf3cf","1"]
]
 
Others=[
  ["Invitation","0xf12f","1","Invitation - MM"],
  ["Profile","0xee35","1","Profile -MM"],
  ["Visiting Card","0xef8f","1","Visiting Card - MM"],
  ["Credit Card","0xef8f","1","Credit card - MM"],
  ["Gifts","0xef2d","1","Gifts - MM"],
  ["wallet","0xee33","1","Wallet - MM"],
  ["Message","0xf2dd","1","Message - MM"],
  ["","0xf197","1"],
  ["","0xf128","1"],
  ["","0xf440","1"],
  ["","0xf14f","1"]
]
 
 
subtype=[ [[i]+j for j in eval(i)] for i in ["Asset","Liability","Income","Expense","Others"]]
subtype_list=[]
for i in subtype:
   for j in i:
       subtype_list.append(j)
subtype_list_dict=[dict(zip(fields,i))   for i in subtype_list]
print(subtype_list_dict)
'''
typeless_list=[]
for i in Custom:
   typeless_list.append(['']+i)
typeless_list_dict=[dict(zip(fields,i))   for i in typeless_list]
#print(typeless_list_dict)
print(subtype_list_dict+typeless_list_dict)
'''
 
 
 
 
 
 

