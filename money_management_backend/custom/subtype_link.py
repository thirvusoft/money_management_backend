import frappe

class link_document():
    def after_insert(self):
        sub_name = self.link_subtype_name
        frappe.errprint(sub_name)