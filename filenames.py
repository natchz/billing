import zipfile
import os

def file_name(nit,invoice_id, file_type="invoice"):
    NIT = str(nit).rjust(10, "0")
    SEQ = format(invoice_id, 'x').rjust(10, "0")
    if file_type == "invoice":
        f_name = "face_f{nit}{seq}.xml".format(nit=NIT, seq=SEQ)
    elif file_type == "debit":
        f_name = "face_d{nit}{seq}.xml".format(nit=NIT, seq=SEQ)
    elif file_type == "credit":
        f_name = "face_c{nit}{seq}.xml".format(nit=NIT, seq=SEQ)
    return f_name

def ws_zip_file(src_dir,f_name):
    zip_name = "{}ws{}.zip".format(src_dir,f_name[4:-4])
    file_name = f_name
    zf = zipfile.ZipFile(zip_name, mode='w')
    try:
        zf.write(src_dir+file_name,file_name)
    finally:
        zf.close()

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def mft_zip_file(src_dir,file_type,f_name,nit):
    NIT = nit.rjust(10, "0")
    if file_type == "invoice":
        f_name = "mft_f{nit}{seq}.xml".format(nit=NIT, seq=SEQ)
    elif file_type == "debit":
        f_name = "mft_d{nit}{seq}.xml".format(nit=NIT, seq=SEQ)
    elif file_type == "credit":
        f_name = "mft_c{nit}{seq}.xml".format(nit=NIT, seq=SEQ)
    zipf = zipfile.ZipFile(f_name, 'w', zipfile.ZIP_DEFLATED)
    zipdir(src_dir, zipf)
    zipf.close()