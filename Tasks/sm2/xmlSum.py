import urllib
import xml.etree.ElementTree as ET

serviceurl = raw_input('Enter location: ')
if not serviceurl: serviceurl = 'http://python-data.dr-chuck.net/comments_283746.xml'

print 'Retrieving', serviceurl
uh = urllib.urlopen(serviceurl)
data = uh.read()
tree = ET.fromstring(data)

counts = tree.findall('comments/comment')
results = 0
for item in counts:
        results += int(item.find('count').text)
print results
