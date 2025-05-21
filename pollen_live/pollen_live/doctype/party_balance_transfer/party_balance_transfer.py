# Copyright (c) 2025, Nesscale Solutions Pvt Ltd
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from erpnext.accounts.utils import get_balance_on
from frappe.utils import today, nowdate
import json


class PartyBalanceTransfer(Document):
    def validate(self):
        if not self.party_type:
            frappe.throw("Please select Party Type")
        if self.party_type not in ["Customer", "Supplier", "Employee"]:
            frappe.throw("Party Type must be Customer, Supplier, or Employee")
        if self.single_party and not self.party:
            frappe.throw("Please select Party Name")

    def on_submit(self):
        transfer_details = []

        if self.single_party:
            transfer_details += self.process_party(self.party)
        else:
            parties = self.get_parties_by_type()
            for party in parties:
                transfer_details += self.process_party(party.name)

        if transfer_details:
            self.transfer_details = generate_html_table(transfer_details)
            self.save()

    def get_parties_by_type(self):
        doctype_map = {
            "Customer": {"doctype": "Customer", "filters": {"disabled": 0}},
            "Supplier": {"doctype": "Supplier", "filters": {"disabled": 0}},
            "Employee": {"doctype": "Employee", "filters": {"status": "Active"}},
        }
        config = doctype_map[self.party_type]
        return frappe.get_all(
            config["doctype"], filters=config["filters"], fields=["name"]
        )

    def process_party(self, party):
        transfer_details = []
        balance = get_balance_on(self.from_account, today(), self.party_type, party)

        if balance <= 0:
            return []

        party_account = frappe.db.get_value(
            "Party Account",
            {
                "company": self.company,
                "parenttype": self.party_type,
                "parent": party,
            },
            "account",
        )

        if not party_account:
            transfer_details.append(
                {
                    "party_type": self.party_type,
                    "party": party,
                    "from_account": self.from_account,
                    "to_account": party_account,
                    "balance": balance,
                    "error": f"No default account set for {self.party_type} {party}",
                }
            )
            return transfer_details

        if party_account == self.from_account:
            transfer_details.append(
                {
                    "party_type": self.party_type,
                    "party": party,
                    "from_account": self.from_account,
                    "to_account": party_account,
                    "balance": balance,
                    "error": f"No default account set for {self.party_type} {party}",
                }
            )
            return transfer_details

        # self.create_journal_entry(party, party_account, balance)

        if self.party_type == "Customer":
            self.update_customer_invoices(party, party_account)

        transfer_details.append(
            {
                "party_type": self.party_type,
                "party": party,
                "from_account": self.from_account,
                "to_account": party_account,
                "balance": balance,
            }
        )

        return transfer_details

    def create_journal_entry(self, party, to_account, balance):
        je = frappe.new_doc("Journal Entry")
        je.voucher_type = "Journal Entry"
        je.posting_date = nowdate()
        je.remark = (
            f"Transfer balance for {party} from {self.from_account} to {to_account}"
        )

        je.append(
            "accounts",
            {
                "account": to_account,
                "party_type": self.party_type,
                "party": party,
                "debit": balance,
                "credit": 0,
                "debit_in_account_currency": balance,
                "credit_in_account_currency": 0,
            },
        )

        je.append(
            "accounts",
            {
                "account": self.from_account,
                "party_type": self.party_type,
                "party": party,
                "debit": 0,
                "credit": balance,
                "debit_in_account_currency": 0,
                "credit_in_account_currency": balance,
            },
        )

        je.save()
        je.submit()

    def update_customer_invoices(self, party, new_account):
        if not new_account:
            return
        filters = {
            "customer": party,
            "status": ["in", ["Draft", "Unpaid", "Partially Paid", "Overdue"]],
            "debit_to": self.from_account,
        }
        invoices = frappe.get_all("Sales Invoice", filters=filters, fields=["name"])
        for invoice in invoices:
            frappe.db.set_value("Sales Invoice", invoice.name, "debit_to", new_account)
            frappe.db.sql(
                """
				UPDATE `tabGL Entry` 
				SET account=%s 
				WHERE voucher_type='Sales Invoice' AND voucher_no=%s 
				AND party_type=%s AND party=%s
			""",
                (new_account, invoice.name, self.party_type, party),
            )
            frappe.db.sql(
                """
				UPDATE `tabPayment Ledger Entry` 
				SET account=%s 
				WHERE voucher_type='Sales Invoice' AND voucher_no=%s 
				AND party_type=%s AND party=%s
			""",
                (new_account, invoice.name, self.party_type, party),
            )


def generate_html_table(transaction_details_json):
    try:
        if isinstance(transaction_details_json, str):
            data = json.loads(transaction_details_json)
        else:
            data = transaction_details_json
    except Exception as e:
        return f"<p style='color:red;'>Error parsing transaction details: {e}</p>"

    if not data:
        return "<p>No transactions found.</p>"

    html = """
    <table class="table table-bordered table-sm">
        <thead>
            <tr>
                <th>Party Type</th>
                <th>Party</th>
                <th>From Account</th>
                <th>To Account</th>
                <th>Balance</th>
                <th>Error</th>
            </tr>
        </thead>
        <tbody>
    """

    for row in data:
        html += "<tr>"
        html += f"<td>{row.get('party_type', '')}</td>"
        html += f"<td>{row.get('party', '')}</td>"
        html += f"<td>{row.get('from_account', '')}</td>"
        html += f"<td>{row.get('to_account', '')}</td>"
        html += f"<td>{row.get('balance', '')}</td>"
        html += f"<td style='color:red;'>{row.get('error', '')}</td>"
        html += "</tr>"

    html += "</tbody></table>"
    return html
