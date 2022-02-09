import frappe
def create_ts_movable_list():
    movable_list= ['Precious Metal','Vehicle','Purchase']
    for movable in movable_list:
        doc = frappe.new_doc('TS Movable List')
        doc.ts_movable = movable
        doc.insert()