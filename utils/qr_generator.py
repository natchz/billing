import qrcode

def fill_qr_data(NumFac, FecFac, NitFac, DocAdq, ValFac, ValIva, ValOtroIm, ValFacIm, CUFE):
    qr_data={"NumFac":NumFac
    ,"FecFac":FecFac
    ,"NitFac":NitFac
    ,"DocAdq":DocAdq
    ,"ValFac":ValFac
    ,"ValIva":ValIva
    ,"ValOtroIm":ValOtroIm
    ,"ValFacIm":ValFacIm
    ,"CUFE":CUFE}
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
    img.save("qr/{}.png".format(CUFE))

qr_data = fill_qr_data("A02F-00117836", "20140319105605", "808183133", "8081972684", "1000.00", "160.00", "0.00",
                       "1160.00", "2836a15058e90baabbf6bf2e97f05564ea0324a6")
create_qr(qr_data)
