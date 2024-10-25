
from secrets import token_bytes
from typing import Tuple

def random_key(length):
    tb=token_bytes(length)
    return int.from_bytes(tb,'big')

def encrypt(original):
    original_bytes=original.encode()
    print('OB',original_bytes)
    dummy=random_key(len(original_bytes))
    print('D',dummy)
    original_key=int.from_bytes(original_bytes,'big')
    print('OK',original_key)
    encrypted=original_key^dummy
    print('E',encrypted)
    return dummy, encrypted

def decrypt(key1,key2):
    decrypted=key1^key2
    print('DC',decrypted)
    temp=decrypted.to_bytes((decrypted.bit_length()+7)//8,'big')
    return temp.decode()
                            


def main():
    key1,key2=encrypt('One Time Pad')
    print('K1K2',key1,key2)
    result=decrypt(key1,key2)
    print(result)
                


if __name__=="__main__":

    main()





