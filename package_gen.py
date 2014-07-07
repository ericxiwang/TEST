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


def event_id_gen():	#generate the real event_id element
	UU_ID = str(uuid.uuid1())
	cTime = str(int(time.time()))

	event_id = UU_ID+"_"+cTime
	return event_id
def other_elements():
	idfa = "96897318-C87C-4849-8E9C-A40319B7EA05"
	distinct_id = str(int(time.time()))+"6ec5-41dc-939e-6885b3c43867"
	return idfa,distinct_id

def package_generator(event_name,SDK_version,token_id,illegal_data,idfa_enable,debug_mode):

	# 
	if illegal_data == 1:
		ctime = "aabbccdd"
	else:
		ctime = int(time.time())

	if idfa_enable == 1:
		idfa = "96897318-C87C-4849-8E9C-A40319B7EA05"
	else:
		idfa = ""

	if event_name == "YA0birth":
		pass
	elif event_name == "YA0session":
		pass
	elif event_name == "YA0charge":
		pass
	else:
		pass

	event_property = {	
	"distinct_id": other_elements()[1],
   	#"YA0debug": write_into,
   	"YA0ver":SDK_version,
   	"uid": "",
   	"idfa": idfa,
   	"amount": 100.0,
   	"currency": "CNY",
   	"YA0ver": "1.3.0",
   	"YA0token": token_id,
   	"ctime": ctime,
   	"event_id": event_id_gen()
   	}

   	if debug_mode == 1:
   		event_property["YA0debug"] = 1

	template_data = {
 	"event": event_name,

 	"properties": event_property

	}

	


	#if debug_mode == 1:
	#template_data.update("properties",{"YA0debug":1})


	json_data = json.dumps(template_data)
	print json_data

   	transfer_base64 = "data="+base64.b64encode(json_data)
   	return transfer_base64
	





if __name__ == '__main__':
	a = package_generator("aabb","1.3.0","token_id","bbb",1,0)
	print a
