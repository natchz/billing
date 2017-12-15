from db.model import *
from datetime import datetime
from invoice import invoice_to_xml
from utils.qr_generator import create_qr,get_qr_data
from utils import pdf_generator
from security import CUFE
TODAY = datetime.today().date()

def get_customer(cust_id):
    cust = IpClients.select().where(IpClients.client == cust_id).dicts()
    return cust[0]

def get_items(inv_id):
    items = IpInvoiceItems.select().where(IpInvoiceItems.invoice == inv_id).dicts()
    items=items.peek(items.__len__())
    amounts = IpInvoiceAmounts.select().where(IpInvoiceAmounts.invoice == inv_id).dicts()
    amounts=amounts.peek(items.__len__())

    return items,amounts

def get_invoices():
    invoices = IpInvoices.select().where(IpInvoices.invoice_date_created == TODAY)
    Issue = Issuer.select().dicts()
    issuer = Issue[0]
    for invoice in invoices:
        cufe = CUFE(invoice.invoice)
        client = get_customer(invoice.client)
        items,amounts = get_items(invoice.invoice)
        invoice_to_xml(invoice.invoice, client, items,issuer)
        #create_qr(get_qr_data(invoice.invoice))
        #from utils.pdf_generator import loader
        #loader(invoice,client,items,amounts,issuer,cufe)

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

get_invoices()
