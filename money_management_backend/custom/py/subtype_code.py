

fields=["ts_type","ts_subtype","icon_code" ,"fromfe"]
Asset=[
        ["Gold","0xf1dd", "1"],
        ["Silver","0xf1dd","1"],
        ["Platinum","0xf1dd","1"],
        ["Diamond","0xf05e7","1"],
        ["Vehicles","0xee62","1"],
        ["Home Appliance","0xf447","1"],
        ["Machinery","0xef06","1"],
        ["Agri Land","F104F","1"],
        ["Commercial Land","0xf42b","1"],
        ["Residential Land","0xf1af","1"],
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
        ["Home Appliance","","0"],
        ["Machinery","","0"],
        ["Agricultural Land","","0"],
        ["Residential Land","","0"],
        ["Commercial Land","","0"]
    ]
Liability=[
    ["Debt","0xeea2","1"],
    ["EMI","0xf2d1","1"],
    ["","0xeea2","1"],
    ["","0xf2d1","1"],
    ["","0xe13c","1"],
    ["","0xf0de","1"],
    ["","0xf05ff","1"],
    ["Debt","","0"],
    ["EMI","","0"],

]
Income=[
    ["Salary","0xf04e1","1"],
    ["Asset Sale","0xf2ee","1"],
    ["Scrap Sale","0xf18e","1"],
    ["Rental","0xf244","1"],
    ["Refunds","0xf2d6","1"],
    ["Coupons","0xf3f6","1"],
    ["Lottery","0xf3e8","1"],
    ["Dividends","0xf0617","1"],
    ["Business Profit","0xee35","1"],
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
    ["Dividends","","0"],
    ["Business Profit","","0"]
]
Expense=[
    ["Food","0xf2e9","1"],
    ["Travel","0xf172","1"],
    ["Grocery","0xf37d","1"],
    ["Entertainment","0xf3cf","1"],
    ["Shopping","0xf37f","1"],
    ["Insurance","0xf05f0","1"],
    ["Tax","0xf24e","1"],
    ["Gas","0xf076","1"],
    ["Electricity","0xf016","1"],
    ["Telephone","0xf28c","1"],
    ["Mobile Recharge","0xf28d","1"],
    ["Health","0xf0f2","1"],
    ["Beauty","0xf041","1"],
    ["Electronics","0xef0d","1"],
    ["Gift","0xef2d","1"],
    ["Education","0xf33c","1"],
    ["Maintenance","0xf108","1"],
    ["Social Service","0xf06a4","1"],
    ["Construction","0xf109","1"],
    ["Crop","0xf05ce","1"],
    ["Fertilizer","0xf068b","1"],
    ["","0xf2e9","1"],
    ["","0xf172","1"],
    ["","0xf37d","1"],
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
    ["Invitation","0xf12f","1"],
    ["Profile","0xee35","1"],
    ["Visiting Card","0xef8f","1"],
    ["Credit Card","0xef8f","1"],
    ["Gifts","0xef2d","1"],
    ["wallet","0xee33","1"],
    ["Message","0xf2dd","1"],
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




