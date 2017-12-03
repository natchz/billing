from db.model import *
from datetime import datetime
from invoice import invoice_to_xml

TODAY = datetime.today().date()

def get_customer(cust_id):
    cust = IpClients.select().where(IpClients.client == cust_id).dicts()
    return cust[0]

def get_items(inv_id):
    items = IpInvoiceItems.select(IpInvoiceItems.item_name,IpInvoiceItems.item_description,
                          IpInvoiceItems.item_quantity,IpInvoiceItems.item_price
                          ).where(IpInvoiceItems.invoice == inv_id).dicts()
    return items

def get_invoices():
    invoices = IpInvoices.select().where(IpInvoices.invoice_date_created == TODAY)
    customer = IssuerData.select().dicts()
    customer_nit = customer[0]["nit"]
    for invoice in invoices:
        print(invoice.invoice)
        client = get_customer(invoice.client)
        print(client)
        items = get_items(invoice.invoice)
        for item in items:
            print(item)
        invoice_to_xml(invoice.invoice, client, items,customer_nit)

get_invoices()

