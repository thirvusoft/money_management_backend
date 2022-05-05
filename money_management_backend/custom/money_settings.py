import frappe

@frappe.whitelist(allow_guest=True)
def add_user(user, subtype, type):
  doc=frappe.new_doc("User Permission")

  doc_sub=frappe.get_doc("TS Subtype",subtype)
  backend_sub=frappe.get_all("TS Subtype",filters={'ts_subtype':type,'fromfe':0})
  frappe.errprint(backend_sub)
 
  doc_sub.update({
    'link_type':doc_sub.ts_type,
    'link_subtype':doc_sub.ts_subtype,
    'link_doc_subtype':backend_sub
 
  })
  frappe.errprint("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
  doc_sub.save()
  

  sub_name=doc_sub.ts_subtype
  frappe.errprint(sub_name)
  doc.update({
    'allow':'TS Subtype',
    'user':user,
    'for_value':subtype

  })
  doc.insert(ignore_permissions=True)
  return sub_name
  #return doc.name
  
  # doc=frappe.get_doc('TS Subtype', subtype)
  # users=doc.allow_user
  # user_list=[usr.user for usr in users]
  # if  user not in user_list:
    # doc.update({
    #   'allow_user':users+[{'user':user}]
    # })
  # else:
  #      frappe.throw(("This User Already Exits"))
  # doc.save()
    
  


@frappe.whitelist(allow_guest=True)
def terminate_user(user,subtype):
  doc=frappe.get_all("User Permission", pluck="name",filters={"user":user,"for_value":subtype})
  doc_sub=frappe.get_doc("TS Subtype",subtype)
  sub_name=doc_sub.ts_subtype
  frappe.errprint(sub_name)
  frappe.errprint(user)
  if len(doc):
    for i in doc:
      frappe.delete_doc("User Permission",i ,force=1)
  else:
    frappe.throw(("This User Permission Already Removed"))
  return sub_name
  # doc=frappe.get_doc('User Permission', subtype)
  # users=doc.allow_user
  # user_list=[usr.user for usr in users]
  # if  user in user_list:
  #   for usr in users:
  #     if(usr.user==user):
  #       users.remove(usr)
  # else:
  #   frappe.throw("Role Not assigned for this User")
 
  # doc.update({
  #   'allow_user':users
  # })
  # doc.save()


  