import QuestionClasify.Document as Dt
from nltk.tokenize import word_tokenize

text_D = Dt.main()


def tokenizing_text_to_word():
    document_word = []
    document_sentWord = word_tokenize(text_D)
    for word in document_sentWord:
        document_word.append(word)
    return document_word


def main():
    document_word = tokenizing_text_to_word()
    return document_word
