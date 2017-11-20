import urllib2
import json
year = 2016
maxDays = 0
for m in range(1, 13):
	if(m==2):
		if(year % 4==0):
			maxDays = 30
		else:
			maxDays = 29
	elif(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
		maxDays = 32
	else:
		maxDays = 31
	for d in range(1, maxDays):
		api_date = str(year)
		if(m<10):
			api_date+="0"+str(m)
		else:
			api_date+=str(m)
		if(d<10):
			api_date+="0"+str(d)
		else:
			api_date+=str(d)
		f = urllib2.urlopen('http://api.wunderground.com/api/ee7193fad42bdca9/history_'+api_date+'/q/NY/Ithaca.json')
		json_string = f.read()
		parsed_json = json.loads(json_string)
		#date = parsed_json['history']['date']['pretty']
		temp = parsed_json['history']['dailysummary'][0]['meantempi']
		numHours = len(parsed_json['history']['observations'])
		dictionary = {}
		for i in range(numHours):
			cond = parsed_json['history']['observations'][i]['conds']
			if cond in dictionary:
				dictionary[cond] = dictionary[cond]+1
			else:
				dictionary[cond] = 1
		num = 0
		condition = ""
		for key, value in dictionary.items():
			if value > num:
				num = value
				condition = key
		print "Date: %s, Condition: %s, Temperature: %s" % (api_date, condition, temp)
		f.close()

"""
f = urllib2.urlopen('http://api.wunderground.com/api/ee7193fad42bdca9/history_20170103/q/NY/Ithaca.json')
json_string = f.read()
parsed_json = json.loads(json_string)
date = parsed_json['history']['date']['pretty']
temp = parsed_json['history']['dailysummary'][0]['meantempi']
numHours = len(parsed_json['history']['observations'])
dictionary = {}
for i in range(numHours):
	cond = parsed_json['history']['observations'][i]['conds']
	if cond in dictionary:
		dictionary[cond] = dictionary[cond]+1
	else:
		dictionary[cond] = 1
num = 0
condition = ""
for key, value in dictionary.items():
	if value > num:
		num = value
		condition = key
print "Date: %s, Condition: %s, Temperature: %s" % (date, condition, temp)
f.close()
"""