import zipfile
from db.model import Audit
import os

def file_name(nit, file_type="invoice"):
    NIT = str(nit).rjust(10, "0")
    SEQ = format(Audit.select().order_by(Audit.last_invoice_sequence.desc())
                 .limit(1)[0].last_invoice_sequence, 'x').rjust(10, "0")
    if file_type == "invoice":
        f_name = "face_f{nit}{seq}.xml".format(nit=NIT, seq=SEQ)
    elif file_type == "debit":
        f_name = "face_d{nit}{seq}.xml".format(nit=NIT, seq=SEQ)
    elif file_type == "credit":
        f_name = "face_c{nit}{seq}.xml".format(nit=NIT, seq=SEQ)
    Audit.create(invoice_count = 1)
    return f_name

def ws_zip_file(src_dir,f_name):
    zip_name = "{}ws{}.zip".format(src_dir,f_name[4:-4])
    file_name = f_name
    zf = zipfile.ZipFile(zip_name, mode='w')
    try:
        zf.write(src_dir+file_name)
    finally:
        zf.close()

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def mft_zip_file(src_dir,file_type,f_name,nit):
    NIT = nit.rjust(10, "0")
    SEQ = format(Audit.get(Audit.sent_last_sequence), 'x').rjust(10, "0")
    if file_type == "invoice":
        f_name = "mft_f{nit}{seq}.xml".format(nit=NIT, seq=SEQ)
    elif file_type == "debit":
        f_name = "mft_d{nit}{seq}.xml".format(nit=NIT, seq=SEQ)
    elif file_type == "credit":
        f_name = "mft_c{nit}{seq}.xml".format(nit=NIT, seq=SEQ)
    zipf = zipfile.ZipFile(f_name, 'w', zipfile.ZIP_DEFLATED)
    zipdir(src_dir, zipf)
    zipf.close()

