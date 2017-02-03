# 2017_01_31_JSON_Homework2
import urllib
import json
service_url = 'http://python-data.dr-chuck.net/geojson?'
while True:
    address = raw_input('Enter location:')
    if len(address) < 1 : break

    # add the parameters needed to the url
    # To call the API, you need to provide a sensor=false parameter and
    # the address that you are requesting as the address= parameter that is
    # properly URL encoded using the urllib.urlencode() function
    url = service_url + urllib.urlencode({'sensor': 'false', 'address': address})
    print url
    uh = urllib.urlopen(url)
    data = uh.read()
    js = json.loads(str(data))
    print js
    place_id = js["results"][0]["place_id"]
    print place_id