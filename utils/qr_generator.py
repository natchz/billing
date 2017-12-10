import qrcode
from db.model import *
from security import CUFE

def get_qr_data(invoice_id):

    data,cufe,iva,otro_imp,fac_imp = CUFE(invoice_id)
    qr_data={"NumFac":data[0]
    ,"FecFac":IpInvoices.select(IpInvoices.invoice_date_created).where(IpInvoices.invoice == invoice_id)
    ,"NitFac":data[2]
    ,"DocAdq":data[4]
    ,"ValFac":data[1]
    ,"ValIva":iva
    ,"ValOtroIm":otro_imp
    ,"ValFacIm":fac_imp
    ,"CUFE":cufe}
    return qr_data

def create_qr(qr_data):
    CUFE = qr_data.get("CUFE")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr_data = '\n'.join("{}: {}".format(k, v) for k, v in qr_data.items())
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save("utils/qr/{}.png".format(CUFE))
