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
sunny =  condition.sunnyDates()
cloudy = condition.cloudyDates()
rainy = condition.rainyDates()
snowy = condition.snowyDates()
cold = temperature.coldDates()
medium = temperature.mediumDates()
hot = temperature.hotDates()

#result_sentiment = GetSentiment (documents)
#result_keyphrases = GetKeyPhrases (documents)

#print (json.dumps(json.loads(result_sentiment), indent=4))
#print (json.dumps(json.loads(result_keyphrases), indent=4))

sunny_text=""
cloudy_text=""
rainy_text=""
snowy_text=""
cold_text=""
medium_text=""
hot_text=""

data = documents['documents']
for i in range(len(data)):
	date = data[i]['date']
	ID = data[i]['id']
	text = data[i]['text']
	if date in sunny:
		sunny_text+=text+" "
	elif date in cloudy:
		cloudy_text+=text+" "
	elif date in rainy:
		rainy_text+=text+" "
	else:
		snowy_text+=text+" "
	if date in cold:
		cold_text+=text+" "
	elif date in medium:
		medium_text+=text+" "
	else:
		hot_text+=text+" "

file = open("sunny_text.txt", "w")
file.write(sunny_text.encode('ascii', errors='ignore'))
file.close

file = open("cloudy_text.txt", "w")
file.write(cloudy_text.encode('ascii', errors='ignore'))
file.close

file = open("rainy_text.txt", "w")
file.write(rainy_text.encode('ascii', errors='ignore'))
file.close

file = open("snowy_text.txt", "w")
file.write(snowy_text.encode('ascii', errors='ignore'))
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
	



