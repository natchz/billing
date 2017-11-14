NSMAP = {
	"fe":"http://www.dian.gov.co/contratos/facturaelectronica/v1"
	,"cac":"urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
	,"cbc":"urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
	,"clm54217":"urn:un:unece:uncefact:codelist:specification:54217:2001"
	,"clm66411":"urn:un:unece:uncefact:codelist:specification:66411:2001"
	,"clmIANAMIMEMediaType":"urn:un:unece:uncefact:codelist:specification:IANAMIMEMediaType:2003"
	,"ext":"urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"
	,"qdt":"urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2"
	,"sts":"http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures"
	,"udt":"urn:un:unece:uncefact:data:specification:UnqualifiedDataTypesSchemaModule:2"
	,"xsi":"http://www.w3.org/2001/XMLSchema-instance"}


    fe_e = ElementMaker(
        annotate=False,
        namespace=NSMAP['fe'],
        nsmap=NSMAP
    )
    cac_e = ElementMaker(
        annotate=False,
        namespace=NSMAP['cac'],
        nsmap=NSMAP
    )
    cbc_e = ElementMaker(
        annotate=False,
        namespace=NSMAP['cbc'],
        nsmap=NSMAP)
