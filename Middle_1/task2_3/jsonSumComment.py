import json
import urllib

serviceurl = raw_input('Enter location: ')
if not serviceurl: serviceurl = 'http://python-data.dr-chuck.net/comments_283750.json'

print 'Retrieving', serviceurl
uh = urllib.urlopen(serviceurl)
data = uh.read()
js = json.loads(data)
count = 0
results = 0
for item in js['comments']:
        results += item['count']
        count += 1

print 'count:',str(count)
print results
