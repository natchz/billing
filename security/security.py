import hashlib
from datetime import datetime
from db.model import *
from lxml.builder import ElementMaker
from lxml import etree
import signxml
from signxml import XMLSigner

TODAY = datetime.today().date()

def signed_time():
    return str(datetime.today().now())



def invoice_datetime_java_format(invoice_id):
    invoice = IpInvoices.get(IpInvoices.invoice == invoice_id)
    inv_date = invoice.invoice_date_created
    inv_time = invoice.invoice_time_created
    inv_datetime = datetime.combine(inv_date,inv_time)
    java_format = "%Y%m%d%H%M%S"
    return datetime.strftime(inv_datetime,java_format)

def hash(hash_type, input_text):
    '''Hash input_text with the algorithm choice'''
    hash_funcs = {'MD5' : hashlib.md5,
                  'SHA1' : hashlib.sha1,
                  'SHA224' : hashlib.sha224,
                  'SHA256' : hashlib.sha256,
                  'SHA384' : hashlib.sha384,
                  'SHA512' : hashlib.sha512}
    return hash_funcs[hash_type](input_text).hexdigest()


def cert_hash():
    with open("security/certificates/certificate.crt","r") as c:
        cert = c.read().encode('utf-8')
        return hash("SHA1", cert)

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

    cursor = database.execute_sql("""
SELECT i.invoice_number,ia.invoice_item_subtotal,id.nit,
case when cc.client_custom_fieldid = 3 and cc.client_custom_fieldvalue = ''
then "01"
when cc.client_custom_fieldid = 3 and cc.client_custom_fieldvalue = 7
then "01"
when cc.client_custom_fieldid = 3 and cc.client_custom_fieldvalue = 8
then "02"
end,cl.client_vat_id, "tec_key"
FROM ip_invoices AS i, ip_clients AS cl, ip_invoice_amounts AS ia, ip_invoice_tax_rates it, issuerdata AS id,
ip_client_custom AS cc
WHERE i.invoice_id = {} AND i.client_id = cl.client_id AND ia.invoice_id = i.invoice_id AND cc.client_id = cl.client_id
LIMIT 1
""".format(invoice_id))

    data = cursor.fetchone()
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


signs = {"ds": "http://www.w3.org/2000/09/xmldsig#"}
sig_maker = ElementMaker(namespace=signs.get("ds"), nsmap=signs)
sig_att = {"Id": "placeholder"}

xades_ns = {"xades":"http://uri.etsi.org/01903/v1.3.2#",
"xades141":"http://uri.etsi.org/01903/v1.4.1#"}

xades_maker = ElementMaker(namespace=xades_ns.get("xades"),nsmap=xades_ns)

def get_xades():

    att_sha1 =  {"Algorithm":"http://www.w3.org/2000/09/xmldsig#sha-1"}
    xades = sig_maker.Object(xades_maker.QualifyingProperties(xades_maker.SignedProperties(xades_maker.SignedSignatureProperties(xades_maker.SigningTime(signed_time()),

                                                                                                                xades_maker.SigningCertificate(
                                                                                                        xades_maker.Cert(xades_maker.CertDigest(
                                                                                                                sig_maker.DigestMethod(att_sha1),
                                                                                                               sig_maker.DigestValue(cert_hash())),
                                                                                                                xades_maker.IssuerSerial(

                                                                                                            sig_maker.X509IssuerName,
                                                                                                                sig_maker.X509SerialNumber)),
                                                                                                        xades_maker.Cert(xades_maker.CertDigest(
                                                                                                                sig_maker.DigestMethod(att_sha1),
                                                                                                                sig_maker.DigestValue(cert_hash())),
                                                                                                            xades_maker.IssuerSerial(
                                                                                                                sig_maker.X509IssuerName,
                                                                                                                sig_maker.X509SerialNumber)),
                                                                                                        xades_maker.Cert(xades_maker.CertDigest(
                                                                                                                sig_maker.DigestMethod(att_sha1),
                                                                                                                sig_maker.DigestValue(cert_hash())),
                                                                                                            xades_maker.IssuerSerial(sig_maker.X509IssuerName,
                                                                                                                sig_maker.X509SerialNumber)))
                                                                                                    ,
                                                                                                    xades_maker.SignaturePolicyIdentifier(
                                                                                                        xades_maker.SignaturePolicyId(
                                                                                                            xades_maker.SigPolicyId(
                                                                                                                xades_maker.Identifier)
                                                                                                            ,
                                                                                                            xades_maker.SigPolicyHash(
                                                                                                                sig_maker.DigestMethod(Algorithm="http://www.w3.org/2000/09/xmldsig#sha-1")
                                                                                                                ,
                                                                                                                sig_maker.DigestValue)))

                                                                                                    ,
                                                                                                    xades_maker.SignerRole(
                                                                                                        xades_maker.ClaimedRoles(
                                                                                                           xades_maker.ClaimedRole))))))
    return xades


def sign_xml(fname):

    xml_inv = open(fname, "rb").read()
    cert = open("security/certificates/certificate.crt","rb").read()
    key = open("security/certificates/key.key", "rb").read()
    root = etree.fromstring(xml_inv)
    signed_root = XMLSigner(method=signxml.methods.enveloped).sign(root, key=key, cert=cert)
    ns = {"ds":"http://www.w3.org/2000/09/xmldsig#"}
    xades_space = signed_root.find(".//ds:KeyInfo",namespaces =ns)
    xades = get_xades()
    xades_space.addnext(xades)
    etree.ElementTree(signed_root).write(fname, encoding='UTF-8', pretty_print=True,
                                         inclusive_ns_prefixes=True)
    # verified_data = XMLVerifier().verify(signed_root).signed_xml
