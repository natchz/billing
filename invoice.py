"""
__author__ = gdalvarezr
__license__ = MIT
"""
from lxml import builder
from zeep import Client,wsdl,xsd
from zeep.plugins import HistoryPlugin
from csv import reader
import smtplib
from datetime import datetime
#from model import *
#from mail_template import send_mail
from mail_success import send_mail
import base64
#customer nit, username, token,


def send_invoice():

    history = HistoryPlugin()
    wsdl = 'http://localhost/facturaElectronica.wsdl'
    client = Client(wsdl=wsdl, plugins=[history])
    encoded = base64.b64encode(b'data to be encoded')
    #print(client.service.EnvioFacturaElectronica("1015420690", "001", datetime.today(), encoded))
    #print(history.last_sent)
    from lxml import etree as ET
    #
    # <your setup code for zeep here>
    #
    node = client.create_message(client.service, 'EnvioFacturaElectronica', "1015420690", "001", datetime.today(), encoded)
    tree = ET.ElementTree(node)
    tree.write('test.xml', pretty_print=True)

def save_ack(ws_resp):
    #write the ack from the sending fucntion
    pass

def invoice_to_xml(UBLExtensions_0,UBLExtensions_1,UBLVersionID,CustomizationID,
                   ProfileID,ID,UUID,IssueDate,IssueTime,InvoiceTypeCode,Note,
                   DocumentCurrencyCode,AccountingSupplierParty ,
                   AccountingCustomerParty ,TaxTotal,LegalMonetaryTotal,
                   InvoiceLine):
    #http://forums.whirlpool.net.au/archive/1975786
    from lxml import etree
    from lxml.builder import ElementMaker

    NSMAP = {
        "fe": "http://www.dian.gov.co/contratos/facturaelectronica/v1"
        , "cac": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
        , "cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
        , "clm54217": "urn:un:unece:uncefact:codelist:specification:54217:2001"
        , "clm66411": "urn:un:unece:uncefact:codelist:specification:66411:2001"
        , "clmIANAMIMEMediaType": "urn:un:unece:uncefact:codelist:specification:IANAMIMEMediaType:2003"
        , "ext": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"
        , "qdt": "urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2"
        , "sts": "http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures"
        , "udt": "urn:un:unece:uncefact:data:specification:UnqualifiedDataTypesSchemaModule:2"
        , "xsi": "http://www.w3.org/2001/XMLSchema-instance"}

    fe_e = ElementMaker(
        namespace=NSMAP['fe'],
        nsmap=NSMAP
    )

    ext_e = ElementMaker(
        namespace=NSMAP['ext'],
        nsmap=NSMAP)

    cac_e = ElementMaker(
        namespace=NSMAP['cac'],
        nsmap=NSMAP
    )
    cbc_e = ElementMaker(
        namespace=NSMAP['cbc'],
        nsmap=NSMAP
    )
    root = fe_e.Invoice(
    ext_e.UBLExtensions(UBLExtensions_0)
    ,ext_e.UBLExtensions(UBLExtensions_1)
    ,cbc_e.UBLVersionID(UBLVersionID)
    ,cbc_e.CustomizationID(CustomizationID)
    ,cbc_e.ProfileID(ProfileID)
    ,cbc_e.ID(ID)
    ,cbc_e.UUID(UBLVersionID)
    ,cbc_e.IssueDate(IssueDate)
    ,cbc_e.IssueTime(IssueTime)
    ,cbc_e.InvoiceTypeCode(InvoiceTypeCode)
    ,cbc_e.Note(Note)
    ,cbc_e.DocumentCurrencyCode(DocumentCurrencyCode)
    ,fe_e.AccountingSupplierParty(AccountingSupplierParty)
    ,fe_e.AccountingCustomerParty(AccountingCustomerParty)
    ,fe_e.TaxTotal(TaxTotal)
    ,fe_e.LegalMonetaryTotal(LegalMonetaryTotal)
    ,fe_e.InvoiceLine(InvoiceLine)
    )

    #print(etree.tostring(root,xml_declaration=True,encoding='UTF-8',pretty_print=True))
    etree.ElementTree(root).write("inv.xml", xml_declaration=True,encoding='UTF-8',standalone=False,pretty_print=True)


"""

    E = ElementMaker(namespace="XSD_Dian_UBL/DIAN_UBL.xsd",
                     nsmap={'p': "http://my.de/fault/namespace"
                            ,'x':"anoter.x.space"})
    data="data"
    data2= "123"
    my_doc = E.one(E.a(data),E.three(data2))
    print(etree.tostring(my_doc,xml_declaration=True,encoding='UTF-8',pretty_print=True))
    etree.ElementTree(my_doc).write("inv.xml", pretty_print=True)
    """

if __name__ == "__main__":
    invoice_to_xml("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17")
    #send_invoice()
    #flow:
    #read_file > to_xml > to_ws > get_resp > send_html mail


