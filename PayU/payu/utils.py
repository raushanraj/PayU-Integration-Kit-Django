from mezzanine.conf import settings
from hashlib import sha512
KEYS = ['key', 'txnid', 'amount', 'productinfo', 'firstname', 'email',
        'udf1', 'udf2', 'udf3', 'udf4', 'udf5',  'udf6',  'udf7', 'udf8',
        'udf9',  'udf10']

SALT=settings.PAYU_INFO.get('merchant_salt')

def generate_hash(data):
    hash = sha512('')
    all_str=''
    for key in KEYS:
        all_str +=str(data.get(key,''))+"|"
    all_str += SALT
    hash=sha512(all_str)
    print hash.hexdigest().lower()
    return hash.hexdigest().lower()

def verify_hash(data):
    keys = ['key', 'txnid', 'amount', 'productinfo', 'firstname', 'email',
        'udf1', 'udf2', 'udf3', 'udf4', 'udf5',  'udf6',  'udf7', 'udf8',
        'udf9',  'udf10']
    keys.reverse()
    all_str=''
    all_str +=SALT+"|"
    all_str +=str(data.get('status', ''))
    for key in keys:
        all_str+="|"+str(data.get(key,''))
    hash=sha512(all_str)
    return (hash.hexdigest().lower() == data.get('hash'))


