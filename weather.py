import urllib2
import json
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