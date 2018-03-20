import QuestionClasify.DataSet as DS
from nltk.tokenize import sent_tokenize, word_tokenize

text_DS = DS.get_Data_Set()


def tokenizing_text_sent_to_word():
    textWord_Tok_Data = []
    textSent_Tok_Data = sent_tokenize(text_DS)

    for sent in textSent_Tok_Data:
        if sent[0].isupper():
            textWord_Tok_Data.append(word_tokenize(sent))
    return textWord_Tok_Data
