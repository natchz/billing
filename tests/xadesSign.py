

signs = {"ds": "http://www.w3.org/2000/09/xmldsig#"}
sig_maker = ElementMaker(namespace=signs.get("ds"), nsmap=signs)
sig_att = {"Id": "placeholder"}
xades_ns = {"xades":"http://uri.etsi.org/01903/v1.3.2#",
"xades141":"http://uri.etsi.org/01903/v1.4.1#"}
xades_maker = ElementMaker(namespace=xades_ns.get("xades"),nsmap=xades_ns)
def get_xades_deprecated():

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
def sign_xml_deprecated(fname):

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
