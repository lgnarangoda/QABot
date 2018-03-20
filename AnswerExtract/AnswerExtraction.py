import AnswerExtract.NumType as NumType
import AnswerExtract.HumType as HumType
import AnswerExtract.LocType as LocType
import nltk
common_words = ["the", "a", "an", "is", "are", "were", ".",]


def AnswerExtracter(document,type1,target):
    
    done = False
    Isanswer = False
    Cananswer = False 
    answer =""
    final_answer=""
    searchwords = set(target).difference(common_words)
    
    for (sentence_no,sentence) in  document:
            
#            ner = NER.corenlp1(sentence)
            # Attempt to find matching substrings
            searchstring = ' '.join(target)
            searchstring = searchstring.lower()
            sentence1 = sentence.lower()
            word = nltk.word_tokenize(sentence)
            
            if searchstring in sentence:
                
                #there is a answer
#                pro_word = Pronounres.pronounres(sentence_no)
#    ##            startidx = sentence.index(target[0])
#    ##            endidx = sentence.index(target[-1])
#                answer = sentence[:startidx]+"(pro - "+str(pro_word)+")"
                answer = answer+"---"+ sentence1#+"(pro - "+str(pro_word)+")"
                Isanswer = True
#                done = False
            # Check if solution is found
            if done:
                continue
            
            # Check by question type
            for w in word:
                
                #Find for atleast one matching word
                tempword = nltk.stem.wordnet.WordNetLemmatizer().lemmatize(w,'v')
                for w1 in searchwords:      
                    tempword2 = nltk.stem.wordnet.WordNetLemmatizer().lemmatize(w1,'v')
                    if tempword == tempword2:
                        #there can be a answer
                        Cananswer = True
                        break          
            
            
            if(type1) == "NUM":
                        answer1 = NumType.NumtypeQuestion(sentence_no,sentence,target)
                        if len(answer1)>0:
                            answer = answer + " " +str(answer1)
                            done = True
                        elif done:
                            break
            if(type1) == "HUM":
                        answer1 = HumType.HumtypeQuestion(sentence_no,sentence,target)
                        if len(answer1)>0:
                            answer = answer + " " +str(answer1)
                            done = True
                        elif done:
                            break
            if(type1) == "LOC":
                        answer1 = LocType.LoctypeQuestion(sentence_no,sentence,target)
                        if len(answer1)>0:
                            answer = answer + " " +str(answer1)
                            done = True
                        elif done:
                            break
    #            w = w.split(sep, 1)[0]
    #            w =  "".join(c for c in w if c not in bad_chars)
#                if w in ner:
#                    if(type1) == "HUM":
#                        if ner[w.lower()] == "PERSON":
##                            startidx = sentence.index(w)
#                            answer = answer + " " +"("+w+")"
#                            done = True
#                        elif done:
#                            break
#            
#                    if(type1) == "LOC":
#                        if ner[w.lower()] == "LOCATION":
#                            answer = answer + " " +w
#                            done = True
#                        elif done:
#                            break
#            
#                    if(type1) == "NUM":
#                        answer1 = how_many.NumtypeQuestion(sentence_no,sentence)
#                        if len(answer1)>0:
#                            answer = answer + " " +w
#                            done = True
#                        elif done:
#                            break
#                            
#                    if(type1) == "TIME":
#                        if ner[w.lower()] == "NUMBER":
#                              answer = answer + " " +w
#                              done = True
#                        if ner[w.lower()] == "DATE":
#                            answer = answer + " " +w
#                            done = True    
#                        elif done:
#                              break
                                          
    if done and Cananswer:
        final_answer = answer

    if Cananswer and done is False: #and Isanswer is False: 
        (sentno,sent) = document[0]
        final_answer = "this is the most matched answer : "+ sent

    if Cananswer is False and Isanswer is False:
        final_answer = "No maching answer found"

    return final_answer
