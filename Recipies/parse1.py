from urllib.request import urlopen
from xml.etree.ElementTree import parse, Element
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#u=urlopen('http://planet.python.org/rss20.xml',context=ctx)
##doc=parse('pred.hml')
##root=doc.getroot()
##print(dir(root))
##print(root)
##root.remove(root.find('cr'))
##print(root.getchildren().index(root.find('sri')))
##print(root.getchildren()[2].getchildren()[1].text)
##
##e=Element('spam')
##e.text='This is a test'
##root.insert(2,e)
##print(root)
##doc.write('newpred.xml',xml_declaration=True)
##
doc=parse('names.xml')
doc.findtext('author')
print(doc.findtext('author'),doc.find('content'))
print(doc.find('content/html'))
print(doc.find('content/{http://www.w3.org/1999/xhtml}html'))
print(doc.findtext('content/{http://www.w3.org/1999/xhtml}html/{http://www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}title'))


class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)
    def register(self, name, uri):
        self.namespaces[name] = '{'+uri+'}'
    def __call__(self, path):
        return path.format_map(self.namespaces)


ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
print(ns)
print(doc.find(ns('content/{html}html')))
