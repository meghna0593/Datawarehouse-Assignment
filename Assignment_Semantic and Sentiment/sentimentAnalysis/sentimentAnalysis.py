import csv
import re
import sys

stopWords_file = open('stopwords.txt','r')
stopWords = stopWords_file.read()
stopWords_file.close()

positiveWords_file = open('positive-words.txt','r')
positiveWords = positiveWords_file.read()
positiveWords_file.close()

negativeWords_file = open('negative-words.txt','r')
negativeWords = negativeWords_file.read()
negativeWords_file.close()

stemThese = ['al','ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment','able']

with open('allTweets.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    my_tweets = []
    for row in csv_reader:
        my_tweets.append(row[0])
#print my_tweets

#removing stop words and numbers
cleanTweets= []
for tweetLine in my_tweets:
    resultTweet = [x for x in tweetLine.lower().split(' ') if x not in stopWords]
    #resultTweet = [i[:-len(j)] for i in resultTweet for j in stemThese if i.endswith(j)]
    resultTweet = ' '.join([str(x) for x in resultTweet])
    resultTweet = ''.join([i for i in resultTweet if not i.isdigit()])
    cleanTweets.append(resultTweet)

#print(cleanTweets)

sentimentFile = csv.writer(open("sentimentTweets.csv", "wb+"))
sentimentFile.writerow(["actual_tweets","final_sentiment","clean_tweets","positive_count","negative_count"])

pos_tweets=0
neg_tweets=0

for i in range(0,len(cleanTweets)):
    pos_count = 0
    neg_count = 0
    resultString = "Not identified"

    for j in positiveWords.splitlines():
        if j in cleanTweets[i]: 
            pos_count+=1
    
    for k in negativeWords.splitlines():
        if k in cleanTweets[i]:
            neg_count+=1
    
    if(pos_count > neg_count):
        resultString="Positive"
        pos_tweets+=1
    elif(pos_count<neg_count):
        resultString="Negative"
        neg_tweets+=1
    elif(pos_count==neg_count):
        resultString="Neutral"
    sentimentFile.writerow([my_tweets[i],resultString,cleanTweets[i],pos_count,neg_count])

print("No. of Positive Tweets:",pos_tweets)
print("No. of Negative Tweets:",neg_tweets)
