import frappe
def create_ts_movable():
    movable_list= ['Precious Metal','Vehicle','Purchase']
    for movable in movable_list:
        doc = frappe.new_doc('TS Movable')
        doc.ts_movable = movable
        doc.insert()