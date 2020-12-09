import hashlib

import datetime




def MakeHash256(s)->str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

def MakeRipemd160(s)->str:
    obj = hashlib.new('ripemd160', s.encode('utf-8'))
    ripemd_160_value = obj.hexdigest()
    return ripemd_160_value



print(MakeHash256("abcdefg"))
print(MakeRipemd160("abcdefg"))

print(datetime.datetime.now())