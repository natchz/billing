from zeep import Client
from zeep.plugins import HistoryPlugin
from datetime import datetime
import base64

def ws_billing_number():
    history = HistoryPlugin()
    wsdl = 'http://www.dian.gov.co/micrositios/fac_electronica/documentos/DIAN_consultaResolucionesFacturacion_ws.wsdl'
    client = Client(wsdl=wsdl, plugins=[history])
    #print(client.service.ConsultaResolucionesFacturacion('1015420690','1015420690','123123'))
    # print(history.last_sent)
    from lxml import etree as ET
    #
    # <your setup code for zeep here>
    #
    node = client.create_message(client.service, 'ConsultaResolucionesFacturacion',
                                 '1015420690','1015420690','123123')
    tree = ET.ElementTree(node)
    tree.write('test_number.xml', pretty_print=True)


def ws_send_invoice(zip_file):
    history = HistoryPlugin()
    wsdl = 'http://localhost/facturaElectronica.wsdl'
    client = Client(wsdl=wsdl, plugins=[history])
    print(zip_file)
    with open(zip_file, "rb") as fh:
        f = fh.read()
    print(f)
    encoded = base64.b64encode(f)
    # print(client.service.EnvioFacturaElectronica("1015420690", "001", datetime.today(), encoded))
    # print(history.last_sent)
    from lxml import etree as ET
    #
    # <your setup code for zeep here>
    #
    node = client.create_message(client.service, 'EnvioFacturaElectronica', "1015420690", "001", datetime.today(),
                                 encoded)
    tree = ET.ElementTree(node)
    tree.write('test.xml', pretty_print=True)

