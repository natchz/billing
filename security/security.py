import hashlib
from datetime import datetime
from db.model import *
from lxml.builder import ElementMaker
from lxml import etree
from os import remove
import subprocess

TODAY = datetime.today().date()

def invoice_datetime_java_format(create_date):
    java_format = "%Y%m%d%H%M%S"
    return datetime.strftime(create_date,java_format)

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

def CUFE(invoice, invoice_lines,invoice_party,issuer):

    cufe = hash('SHA1', "{}{}{}{}{}{}{}{}{}{}{}{}{}".format(invoice["number"],
                                                            invoice_datetime_java_format(invoice["create_date"]),
                                                            invoice["number"],
                                                            "01","tax",
                                                            "02" ,"tax",
                                                            "03","tax",
                                                            "tax",
                                                            issuer["nit"],
                                                            invoice_party["name"],
                                                            invoice_party["name"],
                                                            invoice_party["name"]).encode('utf-8'))
    return cufe

def sign_invoice(fname):
    print(fname)
    subprocess.check_call(["java","-jar","java_xades/xades_v1.2_linux_signer.jar",fname,fname+"_signed"])
    xml_fn = open(fname+"_signed", "rb").read()
    root = etree.fromstring(xml_fn)
    ns = {"ext": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"}
    ns_s = {"ds": "http://www.w3.org/2000/09/xmldsig#"}
    location = root.findall(".//ext:ExtensionContent", namespaces=ns)
    signtaure = root.find(".//ds:Signature", namespaces=ns_s)
    location[1].append(signtaure)
    etree.ElementTree(root).write(fname,xml_declaration=True, encoding='UTF-8', standalone=False,
                                  pretty_print=True)
    remove(fname+"_signed")
