
import random
import sys
import urllib
import bisect
import uuid
import re
#import urllib2
import sys
import threading
import package_gen_duration
import time
import datetime

url = "http://yax.ymcnetwork.com/track"
#url = "http://10.1.1.33:3000/import"

YA0birth = package_gen_duration.package_generator("YA0birth","2.0.2","8416e32af87f11e284c212313b0ace15",1406140628,1406140628)





try:
	rex = urllib.urlopen(url,YA0birth)




except	urllib.error.HTTPError:
	print "error"


	





