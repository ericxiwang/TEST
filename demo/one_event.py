import random
import sys
import urllib
#import urllib2
import sys
import threading
import package_gen_demo 
url = "http://yax.ymcnetwork.com/track"



	




date_1 = [2014,6,15]
time_1 = [random.randint(8,23),30,00]
random_id = str(random.randint(1,500))
data = package_gen_demo.package_generator("YA0birth","2.0.2","8416e32af87f11e284c212313b0ace15",date_1,time_1,random_id)
print data

		
rex = urllib.urlopen(url,data)
print rex.read()


#print "--",x,"--","<",y,">",date_1,time_1





