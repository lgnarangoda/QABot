from pycorenlp import StanfordCoreNLP
from pprint import pprint
text = "How many papers in the queue child"
import nltk
def corenlp1(text):
    corenlp = StanfordCoreNLP('http://corenlp.run:80')
    core = corenlp.annotate(str(text),
                       properties={
                           'annotators': "parse,ner",
                           'outputFormat': 'json',
                           'timeout': 100000,
                       })
    coreDict = {}
    print(core)
    l = 0
    for s in core['sentences']:
        for t in s['tokens']:
            originel_text = t['originalText']
            ner = t['ner']
            coreDict[originel_text.lower()] = ner
    

    return coreDict
# def corenlp1(text):
#     tokenized = nltk.word_tokenize(text)
#     tagged = nltk.pos_tag(tokenized)
#     namedEnt = nltk.ne_chunk(tagged)
#     posDict={}
#
#     for pos_couple in tagged:
#         postag = pos_couple[1]
#         word = pos_couple[0]
#         if postag in posDict:
#             posDict[postag].append(word)
#         else:
#             posDict[postag] = [word]
#
#
#     print(posDict)
# corenlp2(text)

# print(corenlp1('Beautiful Ruins is  an absolute masterpiece.”  —Richard Russo, author of   That Old Cape Magic  The Financial Lives   of the Poets A Novel By Jess Walter  ISBN 978-0-06-191605-2 (paperback)  After gambling everything on a an ill- advised business idea, Matthew Prior  wakes up jobless, hobbled with debt,  spying on his wife’s online flirtation,  and six days away from losing his  home.'))
##print corenlp1(text)
