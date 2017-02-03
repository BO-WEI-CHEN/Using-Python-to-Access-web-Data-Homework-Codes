# vim: set fileencoding=utf-8 :
# 2017_01_24
# Extracting Data from XML Homework
import urllib
import xml.etree.ElementTree as ET


url = 'http://python-data.dr-chuck.net/comments_346650.xml'
xml = urllib.urlopen(url).read()
print xml

tree = ET.fromstring(xml)
counts = tree.findall('.//count')
tree.findall('.//count')

total = 0
total_number = 0
for i in counts:
 total += int(i.text)
 total_number += 1
 print '總和', total
 print 'total_number', total_number
print 'Retrieving', url
print "Retrieved", len(xml), 'characters'
