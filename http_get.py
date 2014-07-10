import urllib2
import urllib
import sys
import time


url = 'http://www.ymcnetwork.com/track'
values = {'name' : 'Michael Foord','location' : 'Northampton','language' : 'Python' }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page