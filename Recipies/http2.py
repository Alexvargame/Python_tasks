
import requests


##url = 'http://httpbin.org/post'
##parms = {
## 'name1' : 'value1',
## 'name2' : 'value2'
##}
##headers = {
## 'User-agent' : 'none/ofyourbusiness',
## 'Spam' : 'Eggs'
##}
##
##resp = requests.post(url,data=parms,headers=headers)
##print(resp.text)

resp = requests.head('http://www.python.org/index.html')
print(resp)
status = resp.status_code
last_modified = resp.headers['last-modified']
content_type = resp.headers['content-type']
content_length = resp.headers['content-length']
