import json
from collections import OrderedDict
##from urllib.request import urlopen
##from pprint import pprint
##import ssl
##
##ctx = ssl.create_default_context()
##ctx.check_hostname = False
##ctx.verify_mode = ssl.CERT_NONE
##
##u=urlopen('http://search.twitter.com/search.json?q=python&rpp=1', context=ctx)
##resp=json.loads(u.read().decode('utf-8'))
##pprint(resp)
##                
s = '{"name": "ACME", "shares": 50, "price": 490.1}'

data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)

class JSONObject:
    def __init__(self, d):
        self.__dict__=d

data=json.loads(s,object_hook=JSONObject)
print(data.name)
