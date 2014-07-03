import urllib
import urllib2
import base64
import sys
import json
url = "http://yax.ymcnetwork.com/track"
origanl_data={
 "event": "YA0charge",
 "properties": {
   "distinct_id": "1f6dc06f-6ec5-41dc-939e-6885b3c43867",
   "YA0debug": 1,
   "uid": "",
   "idfa": "96897318-C87C-4849-8E9C-A40319B7EA05",
   "amount": 0.01,
   "currency": "CAD",
   "YA0ver": "1.1.12",
   "YA0token": "8416e32af87f11e284c212313b0ace15",
   "ctime": 1400273911,
   "event_id": "d612ff2c-dd3c-11e3-b57e-1390f19d8f9b_1400273911"
 }
}

json_data = json.dumps(origanl_data)

transfer_base64 = "data="+base64.b64encode(json_data)
print transfer_base64
rex = urllib.urlopen(url,transfer_base64)
print rex.read()
