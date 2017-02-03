# -*- coding:utf-8 -*-
import re
import urllib
from bs4 import BeautifulSoup
url = 'http://python-data.dr-chuck.net/comments_346653.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "lxml")
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print 'TAG:',tag
    print 'URL:',tag.get('href', None)
    print 'Contents:',tag.contents[0]
    print 'Attrs:',tag.attrs
x = str(tags)
type(x)
y = re.findall('[0-9]+', x)
print y
print sum(map(int, y))  # the answer is 2702
