from urllib.request import urlopen
from xml.etree.ElementTree import parse
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

u=urlopen('http://planet.python.org/rss20.xml',context=ctx)
doc=parse(u)

for item in doc.iterfind('channel/item'):
    title=item.findtext('title')
    date=item.findtext('pubDate')
    link=item.findtext('link')

    print(title)
    print(date)
    print(link)
    print()
