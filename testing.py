UBLExtensions		 ,UBLExtensions 		 ,UBLVersionID 		 ,CustomizationID		 ,ProfileID			 ,ID					 ,UUID					 ,IssueDate			 ,IssueTime			 ,InvoiceTypeCode		 ,Note					 ,DocumentCurrencyCode	 ,AccountingSupplierParty ,AccountingCustomerParty ,TaxTotal				 ,LegalMonetaryTotal	 ,InvoiceLine
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
    ext_e = ElementMaker(
        annotate=False,
        namespace=NSMAP['ext'],
        nsmap=NSMAP)

    cac_e = ElementMaker(
        annotate=False,
        namespace=NSMAP['cac'],
        nsmap=NSMAP
    )
    cbc_e = ElementMaker(
        annotate=False,
        namespace=NSMAP['cbc'],
        nsmap=NSMAP)


<ext:UBLExtensions> …… </ext:UBLExtensions> [1]  <cbc:UBLVersionID> …… </cbc:UBLVersionID> [1]  <cbc:CustomizationID> …… </cbc:CustomizationID> [1]  <cbc:ProfileID> …… </cbc:ProfileID> [1]  <cbc:ID> …… </cbc:ID> [1]  <cbc:UUID> …… </cbc:UUID> [1]  <cbc:IssueDate> …… </cbc:IssueDate> [1]  <cbc:IssueTime> …… </cbc:IssueTime> [1]  <cbc:InvoiceTypeCode> …… </cbc:InvoiceTypeCode> [1]  <cbc:Note> …… </cbc:Note> [0……*]  <cbc:DocumentCurrencyCode> …… </cbc:DocumentCurrencyCode> [1]  <fe:AccountingSupplierParty> …… </fe:AccountingSupplierParty> [1]  <fe:AccountingCustomerParty> …… </fe:AccountingCustomerParty> [1]  <fe:TaxTotal> …… </fe:TaxTotal> [1……*]  <fe:LegalMonetaryTotal> …… </fe:LegalMonetaryTotal> [1]  <tns:InvoiceLine> …… </fe:InvoiceLine> [1……*]
