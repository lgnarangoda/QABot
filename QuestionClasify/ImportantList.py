from nltk.corpus import stopwords
import string
from nltk.tokenize import sent_tokenize, word_tokenize
import  os

def create_punctuation_list():
    punctuation_list = []

    for c in string.punctuation:
        punctuation_list.append(c)
    punctuation_list.append("''")
    punctuation_list.append('``')
    return punctuation_list


def create_stop_word_list():
    stop_word_list = []

    text_stopword_Name = []
    textWord_Tok_feature_Name = []
    cur_path = os.path.dirname(__file__)
    file_stopword_Name = open(cur_path+"/StopWord.txt", mode='r',encoding = "ISO-8859-1")
    text_stopword_Name = file_stopword_Name.read()
    textWord_Tok_stopword_Name = word_tokenize(text_stopword_Name)
    for word in textWord_Tok_stopword_Name:
        stop_word_list.append(word)
    return stop_word_list
