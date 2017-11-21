# -*- coding: utf-8 -*-

import httplib, urllib
import json
import reddit
import condition
import temperature

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the accessKey string value with your valid access key.
accessKey = '6755d6f172a849f8a3756af0c1c31bd5'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your access keys.
# For example, if you obtained your access keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial access keys are generated in the westcentralus region, so if you are using
# a free trial access key, you should not need to change this region.
uri = 'eastus.api.cognitive.microsoft.com'
path_sentiment = '/text/analytics/v2.0/sentiment'
path_keyphrases = '/text/analytics/v2.0/keyPhrases'

def GetSentiment (documents):
    "Gets the sentiments for a set of documents and returns the information."

    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", path_sentiment, body, headers)
    response = conn.getresponse ()
    return response.read ()

def GetKeyPhrases (documents):
    "Gets the sentiments for a set of documents and returns the information."

    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", path_keyphrases, body, headers)
    response = conn.getresponse ()
    return response.read ()


documents = reddit.getDocuments()
data = documents['documents']
sunny =  condition.sunnyDates()
cloudy = condition.cloudyDates()
rainy = condition.rainyDates()
#snowy = condition.snowyDates()
cold = temperature.coldDates()
medium = temperature.mediumDates()
hot = temperature.hotDates()

spring =  condition.springDates()
summer = condition.summerDates()
fall = condition.fallDates()
winter = condition.winterDates()

result_json = GetSentiment(documents)
print result_json
result_sentiment = json.loads(result_json)['documents']

#result_keyphrases = GetKeyPhrases (documents)

#result_sentiment = (json.dumps(json.loads(result_sentiment1), indent=4))
#print (json.dumps(json.loads(result_keyphrases), indent=4))

sunny_score=[]
cloudy_score=[]
rainy_score=[]
#snowy_score=[]
cold_score=[]
medium_score=[]
hot_score=[]

spring_score = []
summer_score = []
fall_score = []
winter_score = []


for i in range(len(result_sentiment)):
	ID = int(result_sentiment[i]['id'])
	for j in range(len(data)):
		if ID == int(data[j]['id']):
			date = data[j]['date']
			if date in sunny:
				sunny_score.append(float(result_sentiment[i]['score']))
			elif date in cloudy:
				cloudy_score.append(float(result_sentiment[i]['score']))
				"""
			elif date in rainy:
				rainy_score.append(float(result_sentiment[i]['score']))
				"""
			else:
				rainy_score.append(float(result_sentiment[i]['score']))
			if date in cold:
				cold_score.append(float(result_sentiment[i]['score']))
			elif date in medium:
				medium_score.append(float(result_sentiment[i]['score']))
			else:
				hot_score.append(float(result_sentiment[i]['score']))
			if date in spring:
				spring_score.append(float(result_sentiment[i]['score']))
			elif date in summer:
				summer_score.append(float(result_sentiment[i]['score']))
			elif date in fall:
				fall_score.append(float(result_sentiment[i]['score']))
			else:
				winter_score.append(float(result_sentiment[i]['score']))



print sunny_score
print cloudy_score
print rainy_score
#print snowy_score
print cold_score
print medium_score
print hot_score

print spring_score
print summer_score
print fall_score
print winter_score

def calculateMean(arr):
	count = 0
	for i in range(len(arr)):
		count+=arr[i]
	return count/float(len(arr))

def calculateMedian(arr):
	arr.sort()
	mid = int(len(arr)/2)
	return arr[mid]

print "Mean"
print "Sunny: "+str(calculateMean(sunny_score))
print "Cloudy: "+str(calculateMean(cloudy_score))
print "Rainy/Snowy: "+str(calculateMean(rainy_score))
#print "Snowy: "+str(calculateMean(snowy_score))
print "Cold: "+str(calculateMean(cold_score))
print "Medium: "+str(calculateMean(medium_score))
print "Hot: "+str(calculateMean(hot_score))
print "Spring: "+str(calculateMean(spring_score))
print "Summer: "+str(calculateMean(summer_score))
print "Fall: "+str(calculateMean(fall_score))
print "Winter: "+str(calculateMean(winter_score))


sunny_text=""
cloudy_text=""
rainy_text=""
cold_text=""
medium_text=""
hot_text=""
spring_text=""
summer_text=""
fall_text=""
winter_text=""

for i in range(len(data)):
	date = data[i]['date']
	ID = data[i]['id']
	text = data[i]['text']
	if date in sunny:
		sunny_text+=text+" "
	elif date in cloudy:
		cloudy_text+=text+" "
	else:
		rainy_text+=text+" "
	if date in cold:
		cold_text+=text+" "
	elif date in medium:
		medium_text+=text+" "
	else:
		hot_text+=text+" "
	if date in spring:
		spring_text+=text+" "
	elif date in summer:
		summer_text+=text+" "
	elif date in fall:
		fall_text+=text+" "
	else:
		winter_text+=text+" "

file = open("sunny_text.txt", "w")
file.write(sunny_text.encode('ascii', errors='ignore'))
file.close

file = open("cloudy_text.txt", "w")
file.write(cloudy_text.encode('ascii', errors='ignore'))
file.close

file = open("rainsnow_text.txt", "w")
file.write(rainy_text.encode('ascii', errors='ignore'))
file.close

file = open("cold_text.txt", "w")
file.write(cold_text.encode('ascii', errors='ignore'))
file.close

file = open("medium_text.txt", "w")
file.write(medium_text.encode('ascii', errors='ignore'))
file.close

file = open("hot_text.txt", "w")
file.write(hot_text.encode('ascii', errors='ignore'))
file.close

file = open("spring_text.txt", "w")
file.write(spring_text.encode('ascii', errors='ignore'))
file.close

file = open("summer_text.txt", "w")
file.write(summer_text.encode('ascii', errors='ignore'))
file.close

file = open("fall_text.txt", "w")
file.write(fall_text.encode('ascii', errors='ignore'))
file.close

file = open("winter_text.txt", "w")
file.write(winter_text.encode('ascii', errors='ignore'))
file.close
	



