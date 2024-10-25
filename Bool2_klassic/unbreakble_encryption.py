from secrets import token_bytes
from typing import Tuple


def random_key(length):
# генерировать Length случайных байтов
    tb= token_bytes(length)
# преобразовать эти байты в битовую строку и вернуть ее
    return int.from_bytes(tb, "big") 


def encrypt(original):
    original_bytes=original.encode()
    print('o_b',original_bytes)
    dummy=random_key(len(original_bytes))
    print('d', dummy)
    original_key=int.from_bytes(original_bytes,'big')
    encrypted=original_key^dummy
    print('o_k', original_key,'en', encrypted)
    return dummy,encrypted
def decrypt(keyl, key2):
    decrypted= keyl^key2
    print('den', decrypted)
    temp=decrypted.to_bytes((decrypted.bit_length()+ 7) // 8, 'big')
    print(temp)
    return temp.decode()

if __name__== "__main__":
    keyl, key2 = encrypt("One Time Pad!")
    result= decrypt(keyl, key2)
    print(result) 
