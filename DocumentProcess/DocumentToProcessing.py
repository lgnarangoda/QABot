import nltk
from bs4 import BeautifulSoup
import collections
import datetime
import os
# sent_detector = nltk.data.load("tokenizers/punkt/english.pickle")
commonwords = ["the", "a", "an", "is", "are", "were", ".", "from"]

# article = ''.join([i if ord(i) < 128 else ' ' for i in article])
###article = lemmatizing.corenlp1(article)

a = datetime.datetime.now()


# pdf reader##########################
# import PyPDF2
# pdfFileObj = open('D:/code/TextFiles/FortyStories.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# pdf_text = ""
#
# pdfReader.numPages
# for x in range(0, pdfReader.getNumPages()): # text is extracted page wise
#		 # A variable to store text extracted from a page
#		pdf_text = pdf_text + pdfReader.getPage(x).extractText() 
# b = datetime.datetime.now()
# print("pdf time - ",b-a)
# html reade#############################
##article = open("cities_a2.htm",'r')
##article = BeautifulSoup(article).get_text()
# article = open("D:/code/TextFiles/FortyStories.txt",'r',encoding="utf8").read()
#################################
# article = open("cities_a2.htm",'r')
# article = BeautifulSoup(article).get_text()


# documenttpprocessing
def DCProcess(target, file):
    # if(file.rsplit('.', 1)[1].lower() == 'pdf'):
    #     import DocumentProcess.pdfreader as pdfreader
    #     pdfreader.convertMultiple(file)
    cur_path = os.path.dirname(__file__)+"/converted_pdf"
    pdf_text = open(cur_path+"/"+ file + ".txt", 'r', encoding="utf8").read()
    # pdf_text = open("D:/ifs final/git/code/DocumentProcess/advs.pdf.txt", 'r', encoding="utf8").read()

    pdf_text = pdf_text.replace("\n", " ")
    pdf_text = pdf_text.replace("\n", ". ")
    pdf_text = nltk.sent_tokenize(pdf_text)
    Document = []
    simple_target = []

    for w in target:
        simple_target.append(w.lower())

    # Remove commonwords
    simple_target = set(simple_target).difference(commonwords)
    dict = collections.Counter()
    dict.clear()
    for (i, sent) in enumerate(pdf_text):
        sentwords = nltk.word_tokenize(sent.lower())

        ##        text = ' '.join([word for word in text.split() if word not in (stopwords.words('english'))])
        wordmatches = set(filter(set(simple_target).__contains__, sentwords))
        dict[sent] = [len(wordmatches), i]

    # Focus on 10 most relevant sentences
    for (sent, sent_no) in dict.most_common(10):
        Document.append([sent_no[1], sent])
    return Document  # print(  DCProcess (['Hayes'])  )
# DCProcess(['ada'],"Homework.txt")
