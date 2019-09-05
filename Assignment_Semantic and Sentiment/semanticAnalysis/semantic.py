import re
import math

contents=[]

for i in range(0, 22):
    if(len(str(abs(i))))==1:
        f=open('reuters/reut2-00'+str(i)+'.sgm', 'r')
    else:
        f=open('reuters/reut2-0'+str(i)+'.sgm', 'r')
    data=f.read()
    f.close()
    cleanData= re.sub('\n|\r', '', data)
    result = re.findall('<BODY>(.*?)</BODY>', cleanData)
    contents.extend(result)

# print(contents)
articleDict = {}
index =0
setOfUniqueWords = set()
wordCountDict = {}

for body in contents:
    flag=0
    articleDict[index] = re.sub(r'[^a-zA-Z0-9]', ' ', body.lower())
    # csvData.writerow([index, articleDict[index]])
    onemorevalue = (articleDict[index]).split(' ')
    for i in onemorevalue:
        if i in wordCountDict.keys():
            #print (i," ",wordCountDict)
            if flag == 0:
                #print i
                wordCountDict[i] += 1
        else:
            wordCountDict[i] = 1
            flag = 1
        setOfUniqueWords.add(str(i))
    print("end of one document")
    index+=1

totalNoOfDocs=len(contents)
del wordCountDict['']

queryCount=wordCountDict['canada']

#IDF Calculation
for k,v in wordCountDict.items():
    print("writing in word")
    wordCountDict[k]=math.log((totalNoOfDocs/v),2)

setOfUniqueWords.remove('')
uniqueWordsDict=(dict.fromkeys(setOfUniqueWords,0))

countArticleSqrd={}
countArticle={}
query={}
query=dict.fromkeys(uniqueWordsDict,0)
query['canada']=1/queryCount #query and query distance
index=0
wordsForArticleSqrd={}
wordsForArticle={}
distance={}
jsonArrayFinal=[]
flag=0

#TF Calculation and Distance
for key1,value1 in articleDict.items():
    print(key1)
    jsonObject={}
    wordsForArticle.clear()
    wordsForArticleSqrd.clear()
    flag=0
    for key2,value2 in uniqueWordsDict.items():
        #wordsForArticle[key2]=0
        if key2 in articleDict.get(key1):
            wordsForArticle[key2]=(1*wordCountDict[key2])
            wordsForArticleSqrd[key2]=math.pow(1*wordCountDict[key2],2)
            if key2=='canada' and flag==0:
                print(key2)
                flag=1
        else:
            wordsForArticle[key2]=0
    #print wordsForArticle
    countArticleSqrd[key1] = math.sqrt(sum(wordsForArticleSqrd.values()))
    countArticle[key1]=wordsForArticle
    #Cosine Similarity
    if flag==1:
        distance[key1]=countArticle[key1]['canada']/countArticleSqrd[key1]
        jsonObject["article"] = "reut_article"+str(key1)
        jsonObject["rank"] = distance[key1]
        jsonObject["content"] = value1
        jsonArrayFinal.append(jsonObject)
#The final output being sorted in descending order by rank
jsonArrayFinalSort = sorted(jsonArrayFinal, key=lambda d: d["rank"],reverse=True)
s=str(jsonArrayFinalSort)
jsonFile = open("finalRank.json","w+")
jsonFile.write(s.replace('\'','\"')); #to rectify json format
jsonFile.close()

#The top-most ranked document
print("The top most rank is:",jsonArrayFinalSort[0]["rank"])
print("The article number:",jsonArrayFinalSort[0]["article"])
print("The content is",jsonArrayFinalSort[0]["content"])


