#!/usr/bin/env python

import urllib2
import json

raw = urllib2.urlopen("http://www.norges-bank.no/api/Currencies/USD?language=no").read()
json_object = json.loads(raw)

today_date = json_object["Daily"]["Values"][0]["DateString"]
f = open('USDNOK_%s.csv' % today_date.replace(".", "") ,'w')

for elem in json_object["Daily"]["Values"]:
    f.write(elem["DateString"] + "," + elem["Value"])
    f.write("\n")

f.close()
