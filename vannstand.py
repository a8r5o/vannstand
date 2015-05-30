#!/usr/bin/env python
#vannstand.py
from urllib2 import urlopen

url = "http://api.sehavniva.no/tideapi.php?"
lang="nb"
lat = "60.395859"
lon = "5.329224"
fromtime = "2015-05-30T00%3A00"
totime = "2015-05-31T00%3A00"
datatype = "tab"
refcode = "cd"
place = ""
api_file = ""
interval = "10"
dts = ""
tzone = ""
tide_request = "locationdata"

url += "?lang=" + lang
url += "&lat=" + lat
url += "&lon=" + lon
url += "&fromtime=" + fromtime
url += "&totime=" + totime
url += "&datatype=" + datatype
url += "&refcode=" + refcode
url += "&place=" + place
url += "&file=" + api_file
url += "&interval=" + interval
url += "&dst=" + dts
url += "&tzone=" + tzone
url += "&tide_request=" + tide_request

print url
response = urlopen(url)
output = response.read()

print output
