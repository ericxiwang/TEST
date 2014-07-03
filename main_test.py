

import urllib
import urllib2
import sys
import threading
import package_gen 
url = "http://yax.ymcnetwork.com/track"

data = package_gen.package_generator("YA0birth","1.3.0","8416e32af87f11e284c212313b0ace15","bbb","1","0")

count = 0
'''
def http_post(url,data):
	rex = urllib.urlopen(url,data)
   	print rex.read()

'''


class ThreadClass(threading.Thread):
	



    def run(self):
    	global data
    	global url
      #  print "%s says Hello World at time: %s" % (self.getName(),now)
        for i in range(1):
        	rex = urllib.urlopen(url,data)
        	global count

       		count = count + 1
        	print count,self.getName()
        	print rex.read()
    




if __name__ == '__main__' :

   #http_post(url,origanl_data)

   #x = http_post(url,origanl_data)
   for i in range(1):


	t = ThreadClass()
	t.start()
'''
   loop = 1



   for i in range(loop):
      x = threading.Thread(target = http_post, args = (url,data))
      x.start()
      print x.getName()

'''

