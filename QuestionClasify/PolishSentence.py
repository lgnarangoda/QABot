from nltk.stem import PorterStemmer
import QuestionClasify.ImportantList as IL

stop_word_list = IL.create_stop_word_list()
punctuation_list = IL.create_punctuation_list()


def remove_case(sentence):
    new_sentence = []
    for sent in sentence:
        sent = sent.lower()
        new_sentence.append(sent)
    return new_sentence


def remove_stopwords(sentence):
    new_sentence = []
    for sent in sentence:
        if sent not in stop_word_list:
            new_sentence.append(sent)
    return new_sentence


def remove_punctuation(sentence):
    new_sentence = []
    for sent in sentence:
        if sent not in punctuation_list:
            new_sentence.append(sent)
    return new_sentence


def stemming_words(sentence):
    ps = PorterStemmer()
    new_sentence = []
    for sent in sentence:
        new_sentence.append(ps.stem(sent))
    return new_sentence


def ignoring_unwanted_words(original_feature_list):
    feature_ignoring_case = remove_case(original_feature_list)
    feature_without_stop_word = remove_stopwords(feature_ignoring_case)
    feature_without_punctuation = remove_punctuation(feature_without_stop_word)
    feature_reducing_stemming = stemming_words(feature_without_punctuation)
    return feature_reducing_stemming
