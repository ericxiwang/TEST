import base64
import sys
import json
import uuid
from datetime import *
import time


def event_id_gen():
	UU_ID = str(uuid.uuid1())
	cTime = str(int(time.time()))

	event_id = UU_ID+"_"+cTime
	return event_id

def package_generator(event_name,SDK_version,token_id,illegal_data,idfa_enable,write_into):


	if illegal_data == 1:
		ctime = "aabbccdd"
	else:
		ctime = 1400273911

	if idfa_enable == 1:
		idfa = "96897318-C87C-4849-8E9C-A40319B7EA05"
	else:
		idfa = ""


	event_id = event_id_gen()

	template_data = {
 	"event": event_name,

 	"properties": {
   	"distinct_id": "1f6dc06f-6ec5-41dc-939e-6885b3c43867",
   	"YA0debug": write_into,
   	"YA0ver":SDK_version,
   	"uid": "",
   	"idfa": idfa,
   	"amount": 100.0,
   	"currency": "CNY",
   	"YA0ver": "1.3.0",
   	"YA0token": token_id,
   	#"ctime": ,
   	"event_id": event_id
 	}
	}

	json_data = json.dumps(template_data)

   	transfer_base64 = "data="+base64.b64encode(json_data)
   	return transfer_base64
	





if __name__ == '__main__':
	a = package_generator("aa","1.3.0","token_id","bbb","0")
	print a
