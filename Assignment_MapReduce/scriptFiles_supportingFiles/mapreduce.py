from __future__ import print_function

import sys
from operator import add
import re
import csv
from pyspark.sql import SparkSession
from pyspark import SparkContext

matchWords=[
        "not safe",
        "safe",
        "accident",
        "long waiting",
        "expensive",
        "friendly",
        "snow storm",
        "good school",
        "good schools",
        "bad school",
        "poor school",
        "bad schools",
        "poor schools",
        "immigrant",
        "immigrants",
        "pollution",
        "bus",
        "buses",
        "park",
        "parks",
        "parking",
        ]


if __name__ == "__main__":

    #collects column 3 from csv file i.e, tweets
    c3 = []
    
    #with open('cleanSearchFile.csv', 'r') as f:
    #with open('cleanStreamFile.csv', 'r') as f:
    with open(sys.argv[1],'r') as f:     #takes file name as argument
        reader = csv.reader(f, delimiter=',')
    
        for row in reader:
            c3.append(row[2])
    
    #starting Spark
    sc = SparkContext('local', 'twitterWordCount') 
    
    #converting words to upper case for consistency
    _str=""
    for i in c3:
        _str += i.upper()

    #splitting words from the string
    words = _str.split()

    #mapping process 
    x=sc.parallelize(words,2)
    mappedWords=x.map(lambda x:(x,1))
    
    #reducing process
    reducedWords=mappedWords.reduceByKey(add).collect()


    finalResult=[]

    #matching keywords with the reduced tuple
    for m in matchWords:
        n = m.upper()
        if(filter(lambda k:n in k,reducedWords)!=[]):
            finalResult.append((filter(lambda k:n in k,reducedWords)[0]))
    
    print('The keywords matching with my data:',finalResult)
    print('The maximum occurred word:',max(finalResult,key=lambda x:x[1]))




