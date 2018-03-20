import AnswerExtract.pos as pos
import nltk
import AnswerExtract.NER as NER
#import Pronounres_V_1
import io
from bs4 import BeautifulSoup
# sent_detector = nltk.data.load("tokenizers/punkt/english.pickle")
#global answer
#answer = []
pro_article = []
noun_dict = {} 
formatted_article = []

def getAnswer(index, sent):
    answer = [] 
    count = 0
        
    for p,w_list in noun_dict.items():
        for w in w_list:
            if w.lower() in sent.lower():
                count = count+1
            
    if count == size:
        ner_dict = NER.corenlp1(sent)
        for keyn, valuen in ner_dict.items():
            if valuen == "LOCATION":
                answer.append(keyn)   
    return answer

def LoctypeQuestion(sentno, sent,question):
    global size 
    size = 0

    postag_dict = pos.corenlp1(question)
    
#    for sent in document:
#        formatted_article.append(" "+sent+" ")
        
           
    for key,value in postag_dict.items():
        if key[0] == "N":
            noun_dict[key] = value
    
    for p,w_list in noun_dict.items():
        for w in w_list:
            size = size+1        
    #size = len(noun_dict)  

    return getAnswer(sentno, sent)
       


        





#if len(answer) == 0:   
# ###############################################   
#    pro_word = Pronounres_V_1.pronounres()  
#    
#    for pro in pro_word:
#        list_size = len(pro)
#        i = 1
#        while list_size > i:
#            sent_index = pro[i][0] - 1
#            word=pro[i][1]
#            new_word=pro[0][1]
#            pro_article.append(formatted_article[sent_index].replace(" "+word+" "," "+new_word+" "))
#            i = i+1
###############
#    for (index, sent) in enumerate(pro_article):              
#        getAnswer(index, sent)
#        
            

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

