from db.model import *
from datetime import datetime
from invoice import invoice_to_xml
from utils.qr_generator import create_qr,get_qr_data
from security.security import CUFE
from utils.pdf_generator import loader
from psql_queries import *
TODAY = datetime.today().date()

###########TODO testing psql ####################

issuer = {"soft_id":"123","soft_security_code":"321321","nit":"00000809-12"}

def psql_invoices():

    invoices = get_invoices('2018-04-27')
    for invoice in invoices:
        #cufe = CUFE(invoice["invoice"])
        cufe = "dummycufe"
        invoice_party = get_party(invoice["party"])[0] #0 as only need first element of party
        invoice_lines = get_invoice_lines(invoice["id"])
        invoice_to_xml(invoice, invoice_lines,invoice_party,cufe,issuer)
        create_qr({"CUFE":"dummycufe"})
        #create_qr(get_qr_data(invoice))
        loader(invoice,invoice_party,invoice_lines,issuer,cufe)

"""
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
"""
