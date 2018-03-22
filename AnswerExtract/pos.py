text = "How many papers in the queue child"

from pycorenlp import StanfordCoreNLP
from pprint import pprint
import nltk


##text = "Jhon"
# def corenlp1(text):
#     corenlp = StanfordCoreNLP('http://corenlp.run:80')
#     core = corenlp.annotate(str(text),
#                        properties={
#                            'annotators': "ner",
#                            'outputFormat': 'json',
#                            'timeout': 100000,
#                        })
#     coreDict = {}
#
#     print(core)
#     word=[]
#
#     l = 0
#     k = len(core['sentences'][0]['tokens'])
# #    coreDict.setdefault(k,[])
#     while(k>l):
#
#         word = str(core['sentences'][0]['tokens'][l]['originalText'])
#         ner = str(core['sentences'][0]['tokens'][l]['pos'])
#         if ner in coreDict:
#             coreDict[ner].append(word)
#         else:
#             coreDict[ner] = [word]
#         l = l+1
#     return coreDict



def corenlp1(text):
    # tokenized = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(text)

    posDict={}

    for pos_couple in tagged:
        postag = pos_couple[1]
        word = pos_couple[0]
        if postag in posDict:
            posDict[postag].append(word)
        else:
            posDict[postag] = [word]


    return(posDict)
# corenlp1(text)
#print corenlp1(text)
#
#{'WRB': 'How', 'NN': 'queue', 6: [], 'JJ': 'many', 'IN': 'in', 'DT': 'the', 'NNS': 'papers'}