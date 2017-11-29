import hashlib

def hash(hash_type, input_text):
    '''Hash input_text with the algorithm choice'''
    hash_funcs = {'MD5' : hashlib.md5,
                  'SHA1' : hashlib.sha1,
                  'SHA224' : hashlib.sha224,
                  'SHA256' : hashlib.sha256,
                  'SHA384' : hashlib.sha384,
                  'SHA512' : hashlib.sha512}
    return hash_funcs[hash_type](input_text).hexdigest()

def CUFE():
    cufe = 0



    return cufe