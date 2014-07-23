import random
import sys
import urllib
#import urllib2
import sys
import threading
import package_gen_demo 
url = "http://10.1.1.33:3000/import"
#url = "http://yax.ymcnetwork.com/track"
#users = file("users.txt","r")


users = open("users.txt",'r').readlines()
#count = len(users)

for x in range(1,31): # normally [1,31]
	
	print "current day",x
	
	for i in range(random.randint(1,x)):

		current_user_1 = random.choice(users)
		current_user = current_user_1.strip('\n')
	
		date_1 = [2014,6,x]
		time_1 = [random.randint(9,22),30,00]	#purchase event happen range(9am to 10pm)
		#random_id = str(random.randint(1,500))
		data = package_gen_demo.package_generator("YA0charge","2.0.2","8416e32af87f11e284c212313b0ace15",date_1,time_1,current_user)
		#print data

		
		rex = urllib.urlopen(url,data)
		#print rex.read()

open("users.txt",'r').close()


		

