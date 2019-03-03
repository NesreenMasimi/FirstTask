
import json
import requests 

num = input("Enter an NPI number :  ")
if (len(num) < 10 ):
	print ("Invalid value")
else :
	test = "first_name"
	resp1 =requests.get("https://npiregistry.cms.hhs.gov/api/?number={}&enumeration_type=&taxonomy_description=&first_name=&last_name=&organization_name=&address_purpose=&city=&state=&postal_code=&country_code=&limit=&skip=&version=1.0".format(num))
	if (resp1.status_code == 200):
		data = json.loads(resp1.text)
		info = data['results']
		lst = info[0]
		perinfo =lst['basic'] 
		print (type(perinfo))
		print ("first name : {} ".format(perinfo['first_name']))
		print ("last name : {} ".format(perinfo['last_name']))
		contactinfo = lst['addresses']
		contactinfo = contactinfo[0] 
		print ("City : {}".format(contactinfo['city']))
		print ("adress : {}".format(contactinfo['address_2']))



	else :
		print (resp1.status_code)


