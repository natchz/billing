import hashlib
from db.model import IpInvoices
from datetime import datetime
from db.model import *

TODAY = datetime.today().date()


def invoice_datetime_java_format(invoice_id):
    invoice = IpInvoices.get(IpInvoices.invoice == invoice_id)
    inv_date = invoice.invoice_date_created
    inv_time = invoice.invoice_time_created
    inv_datetime = datetime.combine(inv_date,inv_time)
    java_format = "%Y%m%d%H%M%S"
    return datetime.strftime(inv_datetime,java_format)


def invoice_seq():
    seq = Audit.get(Audit.last_invoice_sequence)
    total_invoices = IpInvoices.select().count()
    return seq

def hash(hash_type, input_text):
    '''Hash input_text with the algorithm choice'''
    hash_funcs = {'MD5' : hashlib.md5,
                  'SHA1' : hashlib.sha1,
                  'SHA224' : hashlib.sha224,
                  'SHA256' : hashlib.sha256,
                  'SHA384' : hashlib.sha384,
                  'SHA512' : hashlib.sha512}
    return hash_funcs[hash_type](input_text).hexdigest()

def total_taxes(invoice_id,tax_id):
    cursor = database.execute_sql("""
    SELECT SUM(im.item_tax_total) AS total
FROM ip_invoice_items AS ii, ip_invoice_item_amounts AS im
WHERE ii.invoice_id = {} AND ii.item_tax_rate_id = {} AND ii.item_id = im.item_id
GROUP BY item_tax_rate_id
    """.format(invoice_id, tax_id))
    result = cursor.fetchone()
    if not result:
        result = 0
        return result
    return result[0]

def CUFE(invoice_id):
    print(invoice_id)
    cursor = database.execute_sql("""
SELECT i.invoice_number,ia.invoice_item_subtotal,id.nit,
case when cc.client_custom_fieldid = 3 and cc.client_custom_fieldvalue = ''
then "01"
when cc.client_custom_fieldid = 3 and cc.client_custom_fieldvalue = 5
then "01"
when cc.client_custom_fieldid = 3 and cc.client_custom_fieldvalue = 6
then "02"
end,cl.client_vat_id, "tec_key"
FROM ip_invoices AS i, ip_clients AS cl, ip_invoice_amounts AS ia, ip_invoice_tax_rates it, issuerdata AS id,
ip_client_custom AS cc
WHERE i.invoice_id = {} AND i.client_id = cl.client_id AND ia.invoice_id = i.invoice_id AND cc.client_id = cl.client_id
LIMIT 1
""".format(invoice_id))

    data = cursor.fetchone()
    print(data)
    tax_1 = total_taxes(invoice_id,1)
    tax_2 = total_taxes(invoice_id,2)
    tax_3 = total_taxes(invoice_id,3)

    cufe = hash('SHA1', "{}{}{}{}{}{}{}{}{}{}{}{}{}".format(data[0],
                                                            invoice_datetime_java_format(invoice_id),
                                                            data[1],
                                                            "01",tax_1,
                                                            "02" ,tax_2,
                                                            "03",tax_3,
                                                            tax_1,
                                                            data[2],
                                                            data[3],
                                                            data[4],
                                                            data[5]).encode('utf-8'))

    return data,cufe,tax_1,(tax_2+tax_3),(tax_1+tax_2+tax_3)
