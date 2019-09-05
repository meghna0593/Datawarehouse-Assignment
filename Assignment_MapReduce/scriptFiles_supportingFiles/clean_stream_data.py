#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import emoji
import csv
import json

#opening cleaned json file and including commas inbetween json objects to make it a proper json array
with open('consolidated_streaming.json','r') as myFile:
    data=myFile.read().replace('\n\n', ',')

jsonData = json.loads(data)

csvData = csv.writer(open("cleanStreamFile.csv", "wb+"))

#cleaning text
def cleanTextFromUrlEmojiSplChars(text):
    removed_url = re.sub(r'https\:\/\/([^\s]+)',' ',text)
    removed_emojis = re.sub(r'[\W_]+',' ',removed_url , flags=re.LOCALE)
    removed_splChars = re.sub(r'[^a-zA-Z0-9]',' ',removed_emojis)
    return removed_splChars

#storing relevant data into csv file
csvData.writerow(["id","user_name", "tweet", "created_at", "retweet_count"])
for j in jsonData:
    tweet_text = cleanTextFromUrlEmojiSplChars(j['text'])
    user_name = cleanTextFromUrlEmojiSplChars(j['user']['name'])
    csvData.writerow([
       j['id'],
       user_name,
       tweet_text,
       j['created_at'],
       j['retweet_count']
    ])        



