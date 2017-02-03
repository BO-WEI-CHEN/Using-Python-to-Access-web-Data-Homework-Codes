# 2017_01_31_JSON_Homework1
import urllib
import json
url = 'http://python-data.dr-chuck.net/comments_346654.json'

# open url(prompt for a URL and retrieve data from a URL)
url_open = urllib.urlopen(url)

# extract data(JSON)
data = url_open.read()
print data
info = json.loads(data)
print info
print 'User count', len(info)  # there are two objects in the dictionary "info"
print type(info)

# write a for loop to look for the attributes in JSON and calculate the total count
total = 0
for i in info['comments']:
    total += int(i['count'])
    print 'total count', total