# -*- coding:utf-8 -*-
import urllib
from bs4 import BeautifulSoup
url = 'http://python-data.dr-chuck.net/known_by_Slsbil.html'
for i in range(7):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    # Retrieve all of the anchor tags
    tags = soup('a')
    url = tags[18-1].get('href', None)
    # 之所以要[18-1]是因為：在python的list[]或tuple()，甚至是BS的結果bs4.element.ResultSet中，順位一開始為0，並非為1
    # 所以，藉由BeautifulSoup所extract出來的url，根據題目要從第18個名字開始，亦即在bs4.element.ResultSet中為第17順位[18-1]
    print url

# Do you understand that the assignment is
# start -
# enter a url
# read first page using url
# convert to tags
# get 1 link
# convert to url
# print url
# then repeat those steps
# read second page using url
# convert to tags
# get 1 link
# convert to url
# print url
