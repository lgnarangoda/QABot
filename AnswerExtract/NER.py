from pycorenlp import StanfordCoreNLP
from pprint import pprint
corenlp = StanfordCoreNLP('http://corenlp.run:80')

def corenlp1(text):

    core = corenlp.annotate(str(text),
                       properties={
                           'annotators': "parse,ner",
                           'outputFormat': 'json',
                           'timeout': 100000,
                       })
    coreDict = {}

    l = 0
    for s in core['sentences']:
        for t in s['tokens']:
            originel_text = t['originalText']
            ner = t['ner']
            coreDict[originel_text.lower()] = ner
    

    return coreDict


# print(corenlp1('Beautiful Ruins is  an absolute masterpiece.”  —Richard Russo, author of   That Old Cape Magic  The Financial Lives   of the Poets A Novel By Jess Walter  ISBN 978-0-06-191605-2 (paperback)  After gambling everything on a an ill- advised business idea, Matthew Prior  wakes up jobless, hobbled with debt,  spying on his wife’s online flirtation,  and six days away from losing his  home.'))
##print corenlp1(text)
