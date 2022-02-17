import frappe
def create_ts_portable():
    portable_list= ['Precious Metal','Vehicle','Purchase']
    for portable in portable_list:
        doc = frappe.new_doc('TS Portable')
        doc.ts_portable = portable
        doc.insert()