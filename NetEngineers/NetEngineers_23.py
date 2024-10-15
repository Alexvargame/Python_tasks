import csv
import re
from pprint import pprint

import yaml


class IPAddress:
    def __init__(self,ip_mask):
        if re.fullmatch(r'(\d{1,3}\.){3}(\d{1,3})\/\d{1,2}',ip_mask):
            ip, mask = ip_mask.split('/')[0], ip_mask.split('/')[1]
            for item in re.finditer(r'\d{1,3}', ip):
                if int(item[0])>255 or int(item[0])<1:
                    raise ValueError('Incorrect ip')
            self.ip = ip
            for item in re.finditer(r'\d{1,2}', mask):
                if int(item[0])>32 or int(item[0])<8:
                    raise ValueError('Incorrect mask')
            self.mask = mask
        else:
            raise ValueError('Incorrect data')


    def __str__(self):
        return f"IP address {self.ip}/{self.mask}"
    def __repr__(self):
        return f"IP address ({self.ip}/{self.mask})"





def main():
    ip_list=[]
    ip1=IPAddress('255.1.1.1/32')
    print(ip1)
    ip_list.append(ip1)
    print(ip_list)
if __name__ == "__main__":
    main()

#
