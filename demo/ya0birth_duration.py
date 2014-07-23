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
#url = "http://yax.ymcnetwork.com/track"

url = "http://10.1.1.33:3000/import"


def demo_profile(Start_date,Duration):
	ISOFMT='%Y-%m-%d'
	#Start_date = "2014-6-17"
	#Duration = 30
	curtf=datetime.datetime(*time.strptime(time.strftime(Start_date),ISOFMT)[:6])
	return curtf,Duration


demo_attribute = demo_profile("2014-6-22",45)

print demo_attribute

def user_retention():

	user_list_orignal = open("user_log.txt",'r').readlines()

	amount_users = len(user_list_orignal)

	print amount_users

	#dic = eval(user_list_orignal[0])

	#print dic['date'],dic['id']



	for current in range(demo_attribute[1]):	# Check the user list daily

		current_day = current

		#print current_day

		daily_users = []



		for retention_event in range(amount_users):	#browse all the data in list and find matched one

			current_line = eval(user_list_orignal[retention_event])	# select the one dic by day


			user_list = str(current_line['id'])
			user_date = str(current_line['date'])


			number_day =  user_list.split('#')[1]

			#print current_day,"and",number_day

			


			if int(number_day) == int(current_day):		#if data is matched for current, append it into list

				daily_users.append(user_list.strip('\n'))

				print "!!!",daily_users,user_date

	

		day_1 = (50 + random.randint(-10,8)) 

		day_2 = (44 + random.randint(-9,7))

		day_3 = (38 + random.randint(-8,6)) 

		day_4 = (32 + random.randint(-7,5))

		day_5 = (26 + random.randint(-6,4)) 

		day_6 = (20 + random.randint(-5,3))

		day_7 = (14 + random.randint(-4,2))

		day_8 = (8 + random.randint(-3,1))

		fade_list = [day_1,day_2,day_3,day_4,day_5,day_6,day_7,day_8]

		ISOFMT='%Y-%m-%d'
		date_format =datetime.datetime(*time.strptime(time.strftime(user_date),ISOFMT)[:6])
		total_in_list = len(daily_users)
		print "user amount",len(daily_users)
		print "______________"



		for dd in range(len(fade_list)):	# generate 8 days data

			rate_select = fade_list[dd]	#got daily fade rate from list

			start_date_retention = date_format + datetime.timedelta(dd)

			print rate_select,"\n",
			print start_date_retention

			amount_retention_daily = int(total_in_list*fade_list[dd]*0.01)	# this line decide how many users are selected from pool


			for time_offset in range(amount_retention_daily):

				print amount_retention_daily
				print "---",start_date_retention
				form_date = str(start_date_retention)

				timeArray = time.strptime(form_date, "%Y-%m-%d %H:%M:%S")
				timeStamp_1 = int(time.mktime(timeArray))
				distinct_id = daily_users[time_offset]


				data_1 = package_gen_duration.package_generator("YA0start","2.0.2","8416e32af87f11e284c212313b0ace15",timeStamp_1,distinct_id)

				#rex_1 = urllib.urlopen(url,data_1)
				#print rex_1.read()

				print data_1



def event_generator(event_name):

	if event_name == "YA0birth":

		ratio = 10
		# Every time the script generates a bunch of new users, it will clear the file 'users.txt' firstly.
		file_clear = open('users.txt', 'r+')
		file_clear.truncate() 
		file_clear.close()

		log_clear = open('user_log.txt', 'r+')
		log_clear.truncate() 
		log_clear.close()




	elif (event_name == "YA0start") | (event_name == "YA0session"):

		ratio = 20

	elif event_name == "YA0charge":

		ratio = 1

	elif event_name == "YA0retention":

		pass


	for x in range(demo_attribute[1]):		#range of day, x is current day number

		print "total days = ",x

		destf = demo_attribute[0] + datetime.timedelta(x)

		current_date = destf.strftime("%Y-%m-%d")
		#print current_date
		

		y = int(ratio*(x**0.5) + random.randrange(-5,10))

		for i in range(y):
			print y
			date_1 = current_date				
			time_1 = str(random.randint(12,22)) + ":" + "00" +":" +"00"		#Users event send between 0 am to 23 pm

			datetime_1 = str(date_1) + " " + str(time_1)

			print datetime_1

			timeArray = time.strptime(datetime_1, "%Y-%m-%d %H:%M:%S")

			timeStamp = int(time.mktime(timeArray)) 

			print timeStamp

			if event_name == "YA0birth":



				#random_id = str(random.randint(1,500))	#Generate 500 short integer for distinct_id

				random_id = str(uuid.uuid1())

				####################### Country code generate in term of weight in list #########################

				country_list = {'AL':0.1,'AU':0.1,'AT':0.1,'BE':0.1,'BR':0.2,'CA':0.4,'CL':0.1,'CN':0.3,'CO':0.1,'EG':0.1,'FR':0.1,'DE':0.1,'GR':0.1,'HK':0.1,'IN':0.2,'ID':0.1,'IL':0.1,'IT':0.1,'JP':0.2,'KP':0.1,'MX':0.1,'ES':0.1,'SG':0.1,'TR':0.1,'GB':0.1,'US':0.3}
				#weight = {'a':0.3,'b':3.2,'c':2.4}
				items = country_list.keys()
		
				mysum = 0
				breakpoints = [] 
				for ii in items:
				    mysum += country_list[ii]
				    breakpoints.append(mysum)

				def getitem(breakpoints,items):
				    score = random.random() * breakpoints[-1]
				    ii = bisect.bisect(breakpoints, score)
				    return items[ii] 

				country_code = getitem(breakpoints,items)

				##################  Country code generate end ##############################


				distinct_id = str(country_code + "-" + random_id + "#" + str(x))	#Random country_code + random int(1,500)

				user_log = {"id":distinct_id,"date":date_1}

				f = open('user_log.txt', 'a')

				log = str(user_log) +"\n"
				f.write(log)
				f.close()

			else:
				users = open("users.txt",'r').readlines()
				current_user_1 = random.choice(users)
				distinct_id = current_user_1.strip('\n')
				open("users.txt",'r').close()


			data = package_gen_duration.package_generator(event_name,"2.0.2","8416e32af87f11e284c212313b0ace15",timeStamp,distinct_id)


			print data

			
			rex = urllib.urlopen(url,data)
			print rex.read()
if __name__ == '__main__':

	#event_generator("YA0birth")
	event_generator("YA0start")
	event_generator("YA0session")
	event_generator("YA0charge")
	#user_retention()





