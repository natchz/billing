from peewee import RawQuery
from db.model import *


def customer_info(id):
    cust = RawQuery(IpClients, 'select * from ip_clients where client_id = %s', id)
    for customer_info in cust.dicts():
        return  customer_info


def get_items_info(id):
    items = RawQuery(IpInvoiceItems, 'select * from ip_invoice_items where invoice_id = %s', id)
    items_result = []
    for item in items.dicts():
        items_result.append(item)
    return items_result


def get_amounts_info(id):
    amounts = RawQuery(IpInvoiceAmounts, 'select * from ip_invoice_amounts where invoice_id = %s', id)
    amounts_result = []
    for item in amounts.dicts():
        amounts_result.append(item)
    return amounts_result


def get_invoices_id(TODAY):
    invoices_result = []
    invoices = RawQuery(IpInvoices, 'select * from ip_invoices where invoice_date_created = %s ',TODAY)
    for invoice in invoices.dicts():
        invoices_result.append(invoice)
    return  invoices_result


def get_issuer():
    issuer = RawQuery(Issuer, 'select * from issuerdata limit 1')
    for issuer in issuer.dicts():
        return  issuer
