// Copyright (c) 2025, Nesscale Solutions Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on("Party Balance Transfer", {
    refresh(frm) {
        if (frm.doc.transfer_details) {
            frm.fields_dict.transaction_details.$wrapper.html(frm.doc.transfer_details);
        }
    }
});
