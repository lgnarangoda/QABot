import nltk.data
import nltk
# import Pronounres
def answeryesno(document, question):
##    print question
    prev = "no"
    questionstr = ' '.join(question)
    questionstr = questionstr.lower()
    question = nltk.pos_tag(question)
    answer = "no"
    keyword = ""
    for (word,pos) in question:
        if (pos == 'NN' or pos == 'NNS' or pos == 'NNP' or pos == 'NNPS'):
            keyword = word.lower()
            
            answer = "no"

    for (i,sentence) in document:
       # print sentence
        if answer == "yes":
            break
        
        s = nltk.word_tokenize(sentence[1].lower())
##        print s
        if keyword in s:
            #print sentence
            answer = "yes"#yes
            for (word,pos) in question:
##                print word
                if answer == 'no':
##                    print 'p'+answer
                    break
                if (pos != '.') and (word.lower() not in s) and (pos != 'DT') and (word != 'does') and (word != 'do'):
##                    print 'sent no',i
###                    pro = [word,i]
###                    pro_word = Pronounres.pronounres(pro)
##                    print pro_word
###                    if(pro_word.lower() == word):
##                        print ("pro",pro_word.lower())
##                        print s
###                        answer = 'yes'
##                    print answer+'2' 
                    #print word, pos
                    if pos[0] == 'V':
                        tempword = nltk.stem.wordnet.WordNetLemmatizer().lemmatize(word,'v')                       
                        for (w,p) in nltk.pos_tag(s):
                            if p[0] == 'V':
                                tempword2 = nltk.stem.wordnet.WordNetLemmatizer().lemmatize(w,'v')
                                if tempword == tempword2:
                                    answer = 'yes'
                    
                    elif word in document[0]:                       
                        answer = "yes"
                    document[0]
                    if word == "n't" or word == "not":
                        answer = "no";
                if prev == "yes":
                    if (word == "no" or word =="not" or word=="n't"):
                        answer = "no"
                if pos[0] == 'V':
                    prev = "yes"
                else:
                    prev = "no"
##                print answer
    #print questionstr,answer
    return answer
