from invoice import NSMAP
from lxml import etree
import signxml
from signxml import XMLSigner, XMLVerifier

xml_inv = open("f", "rb").read()
root = etree.fromstring(xml_inv)


def _findall(element, query, namespace="ds", anywhere=False):
    namespaces = {"ds":"http://www.w3.org/2000/09/xmldsig#"}
    print(etree.tostring(element))
    print(element)
    q = element
    if anywhere:
        a = q.findall(".//ds:Signature[@Id='placeholder']", namespaces=namespaces)
        print(etree.tostring(a[0]))
    else:
        return element.findall(namespace + ":" + query, namespaces=namespaces)

signature_placeholders = _findall(root, "Signature[@Id='placeholder']", anywhere=True)
print(signature_placeholders)