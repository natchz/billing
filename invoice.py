"""
__author__ = gdalvarezr
__license__ = MIT
"""
import base64
from datetime import datetime
from lxml import etree
from lxml.builder import ElementMaker
from filenames import ws_zip_file, file_name
import pathlib
from security.security import sign_invoice

TODAY = datetime.today().date()
pathlib.Path('invoices/{}'.format(TODAY)).mkdir(parents=True, exist_ok=True)
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
    , "ds": "urn:un:unece:uncefact:data:specification:UnqualifiedDataTypesSchemaModule:2"
    , "xades": "urn:un:unece:uncefact:data:specification:UnqualifiedDataTypesSchemaModule:2"
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
sts_e = ElementMaker(
    namespace=NSMAP['sts'],
    nsmap=NSMAP
)

def invoice_to_xml(invoice_id, client, items, issuer):
    # http://forums.whirlpool.net.au/archive/197578
    # Global Attributes
    uuid_att = {"schemeAgencyID": "195"
        , "schemeAgencyName": "CO, DIAN (Direccion de Impuestos y Aduanas Nacionales)"
        , "schemeName": "CUFE"
        , "schemeURI": "http://www.dian.gov.co/contratos/facturaelectronica/v1/anexo_v1_0.pdf#CUFE"}

    invoice_type_code_att = {"listAgencyID": "195"
        , "listAgencyName": "CO, DIAN (Direccion de Impuestos y Aduanas Nacionales)"
        , "listSchemeURI": "http://www.dian.gov.co/contratos/facturaelectronica/v1/InvoiceType"}

    party_identification_id_att = {"schemeAgencyID": "195"
        , "schemeAgencyName": "CO, DIAN (Direccion de Impuestos y Aduanas Nacionales)"
        , "schemeID": "31"}

    tax_amount_att = {"currencyID": "COP"}

    root = fe_e.Invoice(
        ext_e.UBLExtensions(ext_e.UBLExtension(ext_e.ExtensionContent(sts_e.DianExtensions
            (sts_e.InvoiceControl(sts_e.InvoiceAuthorization("t:NumericType | | xsd: decimal),")
            , sts_e.AuthorizationPeriod(cbc_e.StartDate
            ,cbc_e.EndDate)
            , sts_e.AuthorizedInvoices(
                sts_e.Prefix
                , sts_e.From
                , sts_e.To)
        ),
            sts_e.InvoiceSource(cbc_e.IdentificationCode("qdt:CountryIdentificationCodeType || xsd:string)"
                )),
            sts_e.SoftwareProvider(
            sts_e.ProviderID
            , sts_e.SoftwareID(issuer["soft_id"]))
            , sts_e.SoftwareSecurityCode(
            issuer["soft_security_code"])
        ))),
            ext_e.UBLExtension(ext_e.ExtensionContent(
                )))
            , cbc_e.UBLVersionID()
            , cbc_e.CustomizationID()
            , cbc_e.ProfileID()
            , cbc_e.ID()
            , cbc_e.UUID(uuid_att)
            , cbc_e.IssueDate()
            , cbc_e.IssueTime()
            , cbc_e.InvoiceTypeCode(invoice_type_code_att)
            , cbc_e.Note()
            , cbc_e.DocumentCurrencyCode("COP")
            , fe_e.AccountingSupplierParty(
                cbc_e.AdditionalAccountID("codigo tipo perosna")
                , fe_e.Party(cac_e.PartyIdentification(cbc_e.ID(party_identification_id_att))
                             , cac_e.PartyName(cbc_e.Name)
                             , fe_e.PhysicalLocation(fe_e.Address(cbc_e.CitySubdivisionName
                                                                  , cbc_e.CityName("bogota")
                                                                  , cbc_e.CountrySubentity
                                                                  , cac_e.AddressLine(
                            cbc_e.Line("LESOTO mall Av. 1 street"))
                                                                  , cac_e.Country(cbc_e.IdentificationCode("LS"))
                                                                  )),
                             fe_e.PartyTaxScheme(cbc_e.TaxLevelCode("regimen simp,com,no"), cac_e.TaxScheme)
                             , fe_e.PartyLegalEntity(cbc_e.RegistrationName("PJ - 700085375"))
                             ))

            , fe_e.AccountingCustomerParty(cbc_e.AdditionalAccountID("persona natural u otr??o")
                                           , fe_e.Party(cac_e.PartyIdentification(cbc_e.ID(party_identification_id_att))
                                                        , cac_e.PartyName("PJ - 700085375 - Adquiriente FE")
                                                        , fe_e.PhysicalLocation(fe_e.Address(cbc_e.CitySubdivisionName
                                                                                             , cbc_e.CityName(
                            client["client_city"])
                                                                                             , cbc_e.CountrySubentity
                                                                                             , cac_e.AddressLine(
                            cbc_e.Line(client["client_address_1"]))
                                                                                             , cac_e.Country(
                            cbc_e.IdentificationCode(client["client_country"]))
                                                                                             )),
                                                        fe_e.PartyTaxScheme(cbc_e.TaxLevelCode("simp.com. codigo"),
                                                                            cac_e.TaxScheme)
                                                        ,
                                                        fe_e.PartyLegalEntity(cbc_e.RegistrationName("PJ - 700085375"))
                                                        , fe_e.Person(cbc_e.FirstName(client["client_name"])
                                                                      , cbc_e.FamilyName(client["client_surname"])
                                                                      , cbc_e.MiddleName)))
            , fe_e.TaxTotal(cbc_e.TaxAmount(tax_amount_att)
                            ,cbc_e.TaxEvidenceIndicator("true or false")
                            ,fe_e.TaxSubtotal(cbc_e.TaxableAmount(tax_amount_att)
                                             , cbc_e.TaxAmount(tax_amount_att)
                                             , cbc_e.Percent
                                             , cac_e.TaxCategory(
                    cac_e.TaxScheme(
                        cbc_e.ID))))


            , fe_e.LegalMonetaryTotal(cbc_e.LineExtensionAmount(tax_amount_att)
                    ,cbc_e.TaxExclusiveAmount(tax_amount_att)
                    ,cbc_e.PayableAmount(tax_amount_att))

            , *[fe_e.InvoiceLine(
                cbc_e.ID("{}".format(item["item_name"]))
                , cbc_e.InvoicedQuantity("{}".format(item["item_quantity"]))
                , cbc_e.LineExtensionAmount(tax_amount_att)
                , fe_e.Item(cbc_e.Description("{}".format(item["item_description"])))
                , fe_e.Price(cbc_e.PriceAmount(tax_amount_att,"{}".format(item["item_price"])))
            )
                for item in items
                ]
)

    etree.ElementTree(root).write("invoices/{}/{}".format(TODAY, file_name(issuer["nit"], invoice_id)),
                                  xml_declaration=True, encoding='UTF-8', standalone=False,
                                  pretty_print=True)
    sign_invoice("invoices/{}/{}".format(TODAY, file_name(issuer["nit"], invoice_id)))
    ws_zip_file("invoices/{}/".format(TODAY), file_name(issuer["nit"], invoice_id))

def get_xpath():
    from lxml import etree
    with open("inv.xml", "rb") as f:
        data = f.read()
    root = etree.fromstring(data)
    tree = etree.ElementTree(root)
    for e in root.iter():
        print(tree.getpath(e))


if __name__ == "__main__":
    #pass
    get_xpath()
