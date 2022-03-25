 
 
fields=["ts_type","ts_subtype","icon_code" ,"fromfe","account"]
Asset=[
      ["Gold","0xf1dd","1","Gold - MM"],
      ["Silver","0xf1dd","1","Silver - MM"],
      ["Platinum","0xf1dd","1","Platinum - MM"],
      ["Diamond","0xf05e7","1","Diamond - MM"],
      ["Vehicles","0xee62","1","Vehicles - MM"],
      ["Home","0xf447","1","Home - MM"],
      ["Machinery","0xef06","1","Machinery - MM"],
      ["Agri Land","F104F","1","Agri Land"],
      ["Commercial","0xf42b","1","Commercial - MM"],
      ["Estate","0xf1af","1","Estate - MM"],
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
      ["","0xf05ce","1"],
      ["Gold","","0"],
      ["Silver","","0"],
      ["Platinum","","0"],
      ["Diamond","","0"],
      ["Vehicle","","0"],
      ["Home","","0"],
      ["Machinery","","0"],
      ["Agri Land","","0"],
      ["Estate","","0"],
      ["Commercial","","0"]

 
   ]
Liability=[
   ["Debt","0xeea2","1","Debt - MM"],
   ["EMI","0xf2d1","1","EMI - MM"],
   ["","0xeea2","1"],
   ["","0xf2d1","1"],
   ["","0xe13c","1"],
   ["","0xf0de","1"],
   ["","0xf05ff","1"],
   ["Debt","","0"],
   ["EMI","","0"]
   
 
]
Income=[
  ["Salary","0xf04e1","1","Salary - MM"],
  ["Asset Sale","0xf2ee","1","Asset Sale - MM"],
  ["Scrap Sale","0xf18e","1","Scrap Scale - MM"],
  ["Rental","0xf244","1","Rental - MM"],
  ["Refunds","0xf2d6","1","Refunds - MM"],
  ["Coupons","0xf3f6","1","Coupons - MM"],
  ["Lottery","0xf3e8","1","Lottery - MM"],
  ["Dividend","0xf0617","1","Dividend - MM"],
  ["Revenue","0xee35","1","Revenue - MM"],
  ["","0xf04e1","1"],
  ["","0xf2ee","1"],
  ["","0xf18e","1"],
  ["","0xf244","1"],
  ["","0xf2d6","1"],
  ["","0xf3f6","1"],
  ["","0xf3e8","1"],
  ["","0xf0617","1"],
  ["","0xee35","1"],
  ["Salary","","0"],
  ["Asset/Scrap Sale","","0"],
  ["Rental","","0"],
  ["Lottery","", "0"],
  ["Dividend","","0"],
  ["Revenue","","0"]
]
 
Expense=[
  ["Food","0xf2e9","1","Food - MM"],
  ["Travel","0xf172","1","Travel - MM"],
  ["Grocery","0xf37d","1","Grocery - MM"],
  ["Fun","0xf3cf","1","Fun - MM"],
  ["Shopping","0xf37f","1","Shopping - MM"],
  ["Insurance","0xf05f0","1","Insurance - MM"],
  ["Tax","0xf24e","1","Tax - MM"],
  ["Gas","0xf076","1","Gas - MM"],
  ["Power","0xf016","1","Power - MM"],
  ["Telephone","0xf28c","1","Telephone - MM"],
  ["Mobile","0xf28d","1","Mobile - MM"],
  ["Health","0xf0f2","1","Health - MM"],
  ["Beauty","0xf041","1","Beauty - MM"],
  ["Electronic","0xef0d","1","Electronic - MM"],
  ["Gift","0xef2d","1","Gift - MM"],
  ["Education","0xf33c","1","Education - MM"],
  ["Maintain","0xf108","1","Maintain - MM"],
  ["Social","0xf06a4","1","Social - MM"],
  ["Building","0xf109","1","Building - MM"],
  ["Crop","0xf05ce","1","Crop -MM"],
  ["Fertilizer","0xf068b","1","Fertilizer - MM"],
  ["","0xf2e9","1"],
  ["","0xf172","1"],
  ["","0xf37d","1"],
  ["","0xf3cf","1"],
  ["","0xf3cf","1"],
  ["Home Need","","0"],
  ["Travel","","0"],
  ["Insurance","","0"],
  ["Tax","","0"],
  ["Gift","","0"],
  ["Education","","0"],
  ["Social Service","","0"],
  ["Maintenance","","0"],
  ["Construction","","0"],
  ["Agriculture","","0"],
]
 
Others=[
  ["Invite","0xf12f","1","Invite - MM"],
  ["Profile","0xee35","1","Profile -MM"],
  ["Call Card","0xef8f","1","Call Card - MM"],
  ["Credit Card","0xef8f","1","Credit card - MM"],
  ["Gifts","0xef2d","1","Gifts - MM"],
  ["wallet","0xee33","1","Wallet - MM"],
  ["Message","0xf2dd","1","Message - MM"],
  ["","0xf197","1"],
  ["","0xf128","1"],
  ["","0xf440","1"],
  ["","0xf14f","1"],
  ["Invitation","","0"],
  ["Profile","","0"],
  ["Visiting Card","","0"],
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
 
 
 
 
 
 

