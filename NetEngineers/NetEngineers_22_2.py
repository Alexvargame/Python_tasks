import csv
import re
from pprint import pprint

import yaml


class CiscoTelnet:
    def __init__(self,ip,username,password,secret):
        self.ip=ip
        self.username=username
        self.password=password
        self.secret=secret

    def __str__(self):
        return f"{self.ip} - {self.username}- {self.password}- {self.secret}"





def main():
    r1_params = {
        'ip': '192.168.100.1',
        'username': 'cisco',
        'password': 'cisco',
        'secret': 'cisco'}

    r1=CiscoTelnet(**r1_params)
    print(r1)

if __name__ == "__main__":
    main()

#
