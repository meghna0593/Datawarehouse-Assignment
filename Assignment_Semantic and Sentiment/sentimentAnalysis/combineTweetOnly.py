#!/usr/bin/env python

import csv
import array
import os

with open('cleanSearchFile.csv') as f:
    r=csv.reader(f,delimiter=',')
    dict1=[row[2] for row in r]

with open('cleanStreamFile.csv') as f:
    r=csv.reader(f,delimiter=',')
    dict2=[row[2] for row in r]

dict1.extend(dict2)
allTweets=dict1

csvData = csv.writer(open("allTweets.csv", "w+"))
for tweet in allTweets:
    csvData.writerow([tweet])
