###YMCA server site test script###
###Author:Eric Wang	####
###Create data:/5/1/2014####
###script name:package_gen.py#####

import base64
import sys
import json
import uuid
from datetime import *
import time
import random

def date_time_gen(date_info,time_info):
	manual_year = date_info[0]
	manual_month = date_info[1]
	manual_day = date_info[2]
	manual_date = str(str(manual_year)+ "-" + str(manual_month) + "-" + str(manual_day))

	manual_hour = time_info[0]
	manual_min = time_info[1]
	manual_sec = time_info[2]
	manual_time = str(str(manual_hour)+ ":" + str(manual_min) +":"+ str(manual_sec))

	#manual_date_time = "2014-07-11 16:40:00"
	manual_date_time = str(str(manual_date) + " " +  str(manual_time))

	timeArray = time.strptime(manual_date_time, "%Y-%m-%d %H:%M:%S")
	#print timeArray

	#cTime = str(int(time.time()))

	timeStamp = int(time.mktime(timeArray))

	return timeStamp

def event_id_gen():	#generate the real event_id element
	UU_ID = str(uuid.uuid1())
	cTime = str(int(time.time()))

	event_id = UU_ID+"_"+cTime
	return event_id

def package_generator(event_name,SDK_version,token_id,date_info,time_info,distinct_id):

	

	#print country_code

	event_property = {	
	"distinct_id": distinct_id,
   	#"YA0debug": 1,
   	"YA0ver":SDK_version,
   	"uid": "",
   	"num_retries":5,
   	#"amount": 100.0,
   	#"currency": "CNY",

   	"YA0token": token_id,
   	#"ctime": int(time.time()),
   	"ctime":date_time_gen(date_info,time_info),
   	"event_id": event_id_gen()
   	}
 		
   	#main JSON:template_data
	template_data = {
 	"event": event_name,
 	"properties": event_property

	}
	if event_name == "YA0birth":
		'''f = open('users.txt', 'a')

		users = distinct_id + "\n"
		f.write(users)
		f.close()'''
		pass

	elif event_name == "YA0session":
		start_1 = date_time_gen(date_info,time_info)
		length_1 = int(random.randint(20,100))	#session length range (10s to 1000s)
		end_1 = int(start_1 + length_1)
		session_info = {"start":start_1,"length":length_1,"end":end_1}

		event_property.update(session_info)



	elif event_name == "YA0charge":

		amount = random.choice([1.99,2.99,3.99])

		event_property.update({"currency":"CAD","amount":amount})

		

	'''if event_name == "YA0session":
		template_data.update("properties",{"YA0debug":2})'''

	json_data = json.dumps(template_data)
	#print json_data

   	transfer_base64 = "data="+base64.b64encode(json_data)
   	return transfer_base64



if __name__ == '__main__':
	date_1 = [2014,7,13]
	time_1 = [16,40,00]
	aa = package_generator("YA0birth","9.9.9","dbf6f3cad9f511e3b5a722000a97015e",date_1,time_1,"aabb")
	print aa
