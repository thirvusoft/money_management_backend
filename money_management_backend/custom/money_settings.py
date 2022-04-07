import frappe

@frappe.whitelist(allow_guest=True)
def add_user(user, subtype):
  doc=frappe.get_doc('TS Subtype', subtype)
  users=doc.allow_user
  user_list=[usr.user for usr in users]
  if  user not in user_list:
    doc.update({
      'allow_user':users+[{'user':user}]
    })
  else:
       frappe.throw(("This User Already Exits"))
  doc.save()
    
  


@frappe.whitelist(allow_guest=True)
def terminate_user(user,subtype):
  doc=frappe.get_doc('TS Subtype', subtype)
  users=doc.allow_user
  user_list=[usr.user for usr in users]
  if  user in user_list:
    for usr in users:
      if(usr.user==user):
        users.remove(usr)
  else:
    frappe.throw("Role Not assigned for this User")
 
  doc.update({
    'allow_user':users
  })
  doc.save()


  