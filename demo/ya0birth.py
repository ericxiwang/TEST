import random
import sys
import urllib
#import urllib2
import sys
import threading
import package_gen_demo 
#url = "http://yax.ymcnetwork.com/track"

url = "http://10.1.1.33:3000/import"

file_clear = open('users.txt', 'r+')

file_clear.truncate() # Every time the script generates a bunch of new users, it will clear the file 'users.txt' firstly.
file_clear.close()

for x in range(1,31):		#range of day between in one month
	

	y = int(10*(x**0.5) + random.randrange(-5,10))

	for i in range(y):
		date_1 = [2014,6,x]						#Date from 1 to 30
		time_1 = [random.randint(8,23),30,00]	#Users event send between 8 am to 23 pm
		random_id = str(random.randint(1,500))	#Generate 500 short integer for distinct_id

		country_list = ['AL','AU','AT','BE','BR','CA','CL','CN','CO','EG','FR','DE','GR','HK','IN','ID','IL','IT','JP','KP','MX','ES','SG','TR','GB','US']

		country_code = random.choice(country_list)

		distinct_id = str(country_code + "-" + random_id)	#Random country_code + random int(1,500)

		data = package_gen_demo.package_generator("YA0birth","2.0.2","8416e32af87f11e284c212313b0ace15",date_1,time_1,distinct_id)


		print data

		
		rex = urllib.urlopen(url,data)
		print rex.read()


		print "--",x,"--","<",y,">",date_1,time_1





