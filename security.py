import hashlib
from db.model import Audit,IpInvoices
from datetime import datetime

TODAY = datetime.today().date()

def invoice_seq():
    seq = Audit.get(Audit.last_invoice_sequence)
    total_invoices = IpInvoices.select().count()
    Audit.create(Audit.uploaded_date=TODAY,Audit.invoice_count=total_invoices,
                 Audit.last_invoice_sequence=(total_invoices-seq))
    return seq

def hash(hash_type, input_text):
    '''Hash input_text with the algorithm choice'''
    hash_funcs = {'MD5' : hashlib.md5,
                  'SHA1' : hashlib.sha1,
                  'SHA224' : hashlib.sha224,
                  'SHA256' : hashlib.sha256,
                  'SHA384' : hashlib.sha384,
                  'SHA512' : hashlib.sha512}
    return hash_funcs[hash_type](input_text).hexdigest()

def CUFE(NumFac ,FecFac ,ValFac ,CodImp1 ,ValImp1 ,CodImp2 ,ValImp2 ,
         CodImp3 ,ValImp3 ,ValImp ,NitOFE ,TipAdq ,NumAdq ,ClTec):
    cufe = hash('SHA1', "{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(NumFac ,FecFac,
                                                                  ValFac ,CodImp1 ,ValImp1 ,
                                                                  CodImp2 ,ValImp2 , CodImp3 ,
                                                                  ValImp3 ,ValImp ,NitOFE ,
                                                                  TipAdq ,NumAdq ,ClTec).encode('utf-8'))

    return cufe

print(CUFE(1,2,3,4,5,6,7,8,9,0,3,3,2,2))
