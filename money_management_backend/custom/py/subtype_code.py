

fields=["type","sub_type_name","icon"]
Asset=[
        ["Gold","987727"],
        ["Silver","987727"],
        ["Platinum","987727"],
        ["Diamond","984551"],
        ["Vehicles","61026"],
        ["Home Appliance","62535"],
        ["Machinery","61190"],
        ["Agri Land","987245"],
        ["Commercial Land","62507"],
        ["Residential Land","989633"]
    ]
Liability=[
    ["Debt","61090"],
    ["EMI","62161"]
]
Income=[
    ["Salary","61505"],
    ["Asset Sale","62190"],
    ["Scrap Sale","989624"],
    ["Rental","62020"],
    ["Refunds","62166"],
    ["Coupons","62454"],
    ["Lottery","62440"],
    ["Dividends","984599"],
    ["Business Profit","60981"]
]
Expense=[
    ["Food","62185"],
    ["Travel","61810"],
    ["Grocery","62333"],
    ["Entertainment","62415"],
    ["Shopping","62335"],
    ["Clothing","984383"],
    ["Insurance","984560"],
    ["Tax","62030"],
    ["Gas","61558"],
    ["Electricity","61462"],
    ["Telephone","62092"],
    ["Mobile Recharge","62093"],
    ["Health","61682"],
    ["Beauty","61505"],
    ["Electronics","61197"],
    ["Gift","986692"],
    ["Education","62268"],
    ["Maintenance","61704"],
    ["Social Service","984740"],
    ["Construction","61705"],
    ["Crop","984526"],
    ["Fertilizer","984715"]
]
Others=[
    ["Invitation","61743"],
    ["Profile","60981"],
    ["Visiting Card","61327"]
]
Custom=[
     ["Lock","61847"],
    ["Information","61736"],
    ["Thumbs Up","62528"],
    ["Wifi","61775"],
    ["Account Balance","60978"],
    ["Shopping bag","62333"],
    ["Pets","62085"],
    ["Giftcard","61229"],
    ["Favourite","61514"],
    ["Personal Injury","62081"],
    ["Headphones","61677"],
    ["Music","61949"],
    ["Restaurant","61591"],
    ["Hospital","61822"],
    ["Vacation","61473"],
    ["Savings","62262"],
    ["Diamonds","984551"],
    ["Vehicle","61026"],
    ["Home Appliances","62535"],
    ["Scrap Sales","989624"],
    ["Business Profits","60981"],
    ["Foods","62185"],
    ["Maintain","61704"],
    ["Crops","984526"],
    ["Beautify","61505"],
    ["Groceries","62333"],
    ["Asset Sales","62190"],
    ["Invitations","61743"],
    ["Visiting Cards","61327"],
    ["Profiles","60981"]
]
subtype=[ [[i]+j for j in eval(i)] for i in ["Asset","Liability","Income","Expense","Others","Custom"]]
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




