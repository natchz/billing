from db.model import *
from datetime import datetime
from invoice import invoice_to_xml
from utils.qr_generator import create_qr,get_qr_data
from security.security import CUFE
from utils.pdf_generator import loader
from queries import *
TODAY = datetime.today().date()

def get_customer(cust_id):
    cust_info = customer_info(cust_id)
    return cust_info

def get_items(inv_id):
    items = get_items_info(inv_id)
    amounts = get_amounts_info(inv_id)
    return items,amounts

def get_invoices():

    invoices = get_invoices_id(TODAY)
    issuer = get_issuer()

    for invoice in invoices:
        print(invoice)
        cufe = CUFE(invoice["invoice"])
        print(invoice["client"])
        client = get_customer(invoice["client"])
        items,amounts = get_items(invoice["invoice"])
        invoice_to_xml(invoice["invoice"], client, items,issuer)
        create_qr(get_qr_data(invoice["invoice"]))
        loader(invoice,client,items,amounts,issuer,cufe)

def get_debit_notes():
    debit_notes = IpQuotes.select().where(IpQuotes.quote_date_created == TODAY)
    Issue = Issuer.select().dicts()
    issuer = Issue[0]
    for debit_note in debit_notes:
        client = get_customer(debit_note.client)
        items = get_items(debit_note.quote)
        invoice_to_xml(debit_note.quote, client, items, issuer)

def get_credit_notes():
    credit_notes = IpQuotes.select().where(IpQuotes.quote_date_created == TODAY)
    Issue = Issuer.select().dicts()
    issuer = Issue[0]
    for credit_note in credit_notes:
        client = get_customer(credit_note.client)
        items = get_items(credit_note.quote)
        invoice_to_xml(credit_note.quote, client, items, issuer)
