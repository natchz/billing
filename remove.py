import hashlib
from datetime import datetime
from db.model import *
from lxml.builder import ElementMaker
from lxml import etree
import signxml
from signxml import XMLSigner

fname = "inv2_signed.xml"
fname1 = "final.xml"
xml_inv = open(fname, "rb").read()
root = etree.fromstring(xml_inv)


ns = {"ext": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"}
ns_s = {"ds": "http://www.w3.org/2000/09/xmldsig#"}
location = root.findall(".//ext:ExtensionContent", namespaces=ns)
signtaure = root.find(".//ds:Signature", namespaces=ns_s)
#signtaure.get
#elem[0].getparent().remove(elem[0])
location[1].append(signtaure)
etree.ElementTree(root).write(fname1, encoding='UTF-8', pretty_print=True)
