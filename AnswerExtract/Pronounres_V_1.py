from pycorenlp import StanfordCoreNLP
import json
from pprint import pprint
from bs4 import BeautifulSoup
import time
corenlp = StanfordCoreNLP('http://localhost:9000')
#
article = open("document/music_instruments_a4.htm",'r').read()
article = BeautifulSoup(article).get_text()
article = ''.join([i if ord(i) < 128 else ' ' for i in article])
article = article.replace("\n", " . ")
#article = sent_detector.tokenize(article)
#article = "Jhon is a boy he likes mango. Emily is carrot she likes sleep. Bush is founder of Google. He uses python"
pro_list=[]
#i = 5
def pronounres():
    start_time = time.time()

    corefs = corenlp.annotate(str(article),
                           properties={
                               'annotators': "coref",
                               'outputFormat': 'json',
                               'timeout': 100000,
                           })


    coreDict = dict()
    ##pprint(corefs['corefs']['1'][0]['sentNum'])
    ##pprint(corefs['corefs']['1'][1]['sentNum'])

    for p in corefs['corefs']:

        coreDict.setdefault(p,[])
        i = len(corefs['corefs'][str(p)])
        j = 0;
        while(j<i):
                coreDict[p].append([(corefs['corefs'][str(p)][j]['sentNum']),(corefs['corefs'][str(p)][j]['text'])])
                j = j+1
##    pprint(coreDict)             
    for t in coreDict:
        c = len(coreDict[t])
        if c>1:
          pro_list.append(coreDict[t])  
    print(time.time() - start_time)   
    return pro_list    

#print pronounres()  
#    return pro_list

#            k = 0
#            while c > k:
#                if coreDict[t][k][0] == sentId:
#                    pro_list.append(coreDict[t])
#                k=k+1
    
            
#          k = 0  
#          while c>k:  
#            if coreDict[t][1][0]-1==sentId:
#                print coreDict[t][k][1]
#            k = k+1
#            if sentId in 

