# from pycorenlp import StanfordCoreNLP
# import json
# from pprint import pprint
# from bs4 import BeautifulSoup
# corenlp = StanfordCoreNLP('http://localhost:9000')
#
# text = open("D:/code/TextFiles/article.txt",'r').read()
#
# def pronounres(wordmatch):
#
#     corefs = corenlp.annotate(str(text),
#                            properties={
#                                'annotators': "dcoref",
#                                'outputFormat': 'json',
#                                'timeout': 100000,
#                            })
#
#
#     coreDict = dict()
#     ##pprint(corefs['corefs']['1'][0]['sentNum'])
#     ##pprint(corefs['corefs']['1'][1]['sentNum'])
#
#     for p in corefs['corefs']:
#
#         coreDict.setdefault(p,[])
#         i = len(corefs['corefs'][str(p)])
#         j = 0;
#         while(j<i):
#                 coreDict[p].append([(corefs['corefs'][str(p)][j]['sentNum']),(corefs['corefs'][str(p)][j]['text'])])
#                 j = j+1
# ##    pprint(coreDict)
#     for t in coreDict:
#         c = len(coreDict[t])
#         if c>1:
# ##            print coreDict[t][1][0]-1
# ##            print wordmatch[1]
#             if coreDict[t][1][0]-1==wordmatch[1]:
# ##                print coreDict[t][0][1]
#                 return coreDict[t][0][1]
#
