from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.corpus import stopwords
from collections import defaultdict

# import QuestionClasify.Question as Qu
questions = ""


def tokenizing_textQ_sent_to_word():
    textWord_Tok_Q = []
    global questions
    text_Q = questions
    textSent_Tok_Q = sent_tokenize(text_Q)

    for sent in textSent_Tok_Q:
        textWord_Tok_Q.append(word_tokenize(sent))
    return textWord_Tok_Q


def checking_Yes_No_Type(textWord_Tok_RealQue):
    yes_no_type_list = ['am', 'is', 'are', 'was', 'were', 'will', 'shall', 'may', 'might', 'can', 'could', 'has',
                        'have', 'had', 'do', 'does', 'did']
    for sen in textWord_Tok_RealQue:
        if sen[0] in yes_no_type_list:
            return True


def find_Question(textWord_Tok_RealQue):
    pos_tag_list = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "WDT", "WP", "WP$", "WRB", "MD"]
    real_que = ""
    for sen in textWord_Tok_RealQue:
        sen_postag = nltk.pos_tag(word_tokenize(sen[0]))
        if sen_postag[0][1] in pos_tag_list:
            real_que = sen
    return real_que


def checking_List_Type(textWord_Tok_RealQue):
    tp = False
    if len(textWord_Tok_RealQue) > 1:
        real_que = find_Question(textWord_Tok_RealQue)
    else:
        real_que = textWord_Tok_RealQue[0]

    for wd in real_que:
        wd_postag = nltk.pos_tag(word_tokenize(wd))
        if wd == "list" or wd == "lists":
            tp = True
        elif wd_postag[0][1] == 'NNS' or wd_postag[0][1] == 'NNS':
            tp = True
    return tp


##
##    for sen in real_que:
##        for wd in sen:
##            wd_postag=nltk.pos_tag(word_tokenize(wd))
##            if wd=="list" or wd=="lists":
##                tp=True
##            elif wd_postag[0][1]=='NNS' or wd_postag[0][1]=='NNS':
##                tp=True
##            
##    return tp

def checking_type(textWord_Tok_RealQue):
    if checking_Yes_No_Type(textWord_Tok_RealQue):
        main_type = "Yes/No_Type"
    elif checking_List_Type(textWord_Tok_RealQue):
        main_type = "List_Type"
    else:
        main_type = "WH_Type"
    return main_type


def main(question):
    global questions
    questions = question
    textWord_Tok_Q = tokenizing_textQ_sent_to_word()
    main_type = checking_type(textWord_Tok_Q)
    return main_type
