from pycorenlp import StanfordCoreNLP
from pprint import pprint
text = "How many papers in the queue child"
import nltk
import os
def corenlp1(text):
    # corenlp = StanfordCoreNLP('http://corenlp.run:80')
    # core = corenlp.annotate(str(text),
    #                    properties={
    #                        'annotators': "parse,ner",
    #                        'outputFormat': 'json',
    #                        'timeout': 100000,
    #                    })
    # coreDict = {}
    # print(core)
    # l = 0
    # for s in core['sentences']:
    #     for t in s['tokens']:
    #         originel_text = t['originalText']
    #         ner = t['ner']
    #         coreDict[originel_text.lower()] = ner
    cur_path = os.path.dirname(__file__)
    from nltk.tag.stanford import StanfordNERTagger
    st = StanfordNERTagger(cur_path + "/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz",
                           cur_path + "/stanford-ner/stanford-ner.jar")

    print (st.tag((text)))
# def corenlp1(text):
# java_path = "C:\Program Files\Java\jdk1.8.0_45/bin"
# os.environ['JAVAHOME'] = java_path


# print(st.tag('Rami Eid is studying at Stony Brook University in NY'.split()))

# corenlp2(text)

# print(corenlp1('Beautiful Ruins is  an absolute masterpiece.”  —Richard Russo, author of   That Old Cape Magic  The Financial Lives   of the Poets A Novel By Jess Walter  ISBN 978-0-06-191605-2 (paperback)  After gambling everything on a an ill- advised business idea, Matthew Prior  wakes up jobless, hobbled with debt,  spying on his wife’s online flirtation,  and six days away from losing his  home.'))
##print corenlp1(text)
