text = "How many papers in the queue"

from pycorenlp import StanfordCoreNLP
from pprint import pprint
corenlp = StanfordCoreNLP('http://corenlp.run:80')

##text = "Jhon"
def corenlp1(text):

    core = corenlp.annotate(str(text),
                       properties={
                           'annotators': "ner",
                           'outputFormat': 'json',
                           'timeout': 100000,
                       })
    coreDict = {}


    word=[]

    l = 0
    k = len(core['sentences'][0]['tokens'])
#    coreDict.setdefault(k,[])
    while(k>l):
        
        word = str(core['sentences'][0]['tokens'][l]['originalText'])
        ner = str(core['sentences'][0]['tokens'][l]['pos'])
        if ner in coreDict:
            coreDict[ner].append(word)
        else:
            coreDict[ner] = [word]
        l = l+1
    return coreDict

#print corenlp1(text)
#
#{'WRB': 'How', 'NN': 'queue', 6: [], 'JJ': 'many', 'IN': 'in', 'DT': 'the', 'NNS': 'papers'}