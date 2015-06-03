#!/usr/bin/env python
#vannstand.py
from urllib2 import urlopen
import datetime 
import xml.etree.ElementTree as etree  

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

# tide_reqest [stationlist,standardlevels,locationlevels,constituents,obstime,stattime,monthmean,locationdata,tidetable,
# landsearise,languages,service,fileformats]
tide_request = "locationdata"
#lang [nb,nn,en,de,nl,se]
lang="nb"
#Position
lat = "60.395859"
lon = "5.329224"
#To from date in ISO-8601 
fromtime = today.isoformat()
totime = tomorrow.isoformat()
# datatype [TAB,PRE,OBS,ALL]
datatype = "TAB"
refcode = "cd"
place = ""
#"",PDF,XLS,NSKV,TXT(undocumented)
api_file = ""
interval = "10"
dts = ""
tzone = ""

url = "http://api.sehavniva.no/tideapi.php?"
if tide_request == "locationdata" and lat and lon:
	url += "&tide_request=" + tide_request
	url += "&lat=" + lat
	url += "&lon=" + lon
	url += "&fromtime=" + fromtime
	url += "&totime=" + totime 
	if datatype:
		url += "&datatype=" + datatype
	if lang:
		url += "&lang=" + lang
	if refcode:
		url += "&refcode=" + refcode
	if place:
		url += "&place=" + place
	if api_file:
		url += "&file=" + api_file
	if interval:
		url += "&interval=" + interval
	if dts:
		url += "&dst=" + dts
	if tzone:
		url += "&tzone=" + tzone

response = urlopen(url)
xml = response.read()

print xml + "\n"

tree = etree.parse(xml)

