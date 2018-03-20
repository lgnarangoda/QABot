from nltk.tokenize import sent_tokenize, word_tokenize
import pandas
import nltk
from collections import defaultdict
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
import pickle
import numpy as np
from sklearn.preprocessing import Imputer
from sklearn.tree import DecisionTreeClassifier

import QuestionClasify.SpellingChecker as SC
import QuestionClasify.PolishSentence as PS
import QuestionClasify.DataSetSentWordList as DSSWL
import os
cur_path = os.path.dirname(__file__)
# import Question as Qu

question = "sample"
FEATURES = []
LABELS = []
NEWFEATURE = []
laba_val = {'ABBR': 1, 'ENTY': 2, 'DESC': 3, 'HUM': 4, 'LOC': 5, 'NUM': 6}


def get_K_Value(labeltype):
    for nv in laba_val:
        if labeltype == nv:
            k = laba_val[nv]
            return k


def class_classification(textWord_Tok_Que):
    for sen in textWord_Tok_Que:
        feature_Dict = defaultdict(list)
        label_Dict = defaultdict(list)
        laba_val_num = get_K_Value(sen[0])
        label_Dict['key'] = laba_val_num
        features_name = PS.ignoring_unwanted_words(sen[3:])
        coun = 0
        for fea in features_name:
            feature_Dict[coun] = fea
            coun += 1

        FEATURES.append(feature_Dict)
        LABELS.append(label_Dict)


def data_train():
    ##    vec=DictVectorizer()
    imp = Imputer(missing_values='NaN', strategy='median', axis=0)

    ##    X_tests = vec.fit_transform(FEATURES)
    ##    X_test=imp.fit_transform(X_tests)
    ##    x=X_test.toarray()
    ##
    ##    with open('data_train.pickle','wb') as ff:
    ##        pickle.dump(vec,ff)

    pickle_vec = open(cur_path+'/data_train.pickle', 'rb')
    vec = pickle.load(pickle_vec)

    X_trains = vec.transform(NEWFEATURE)
    X_train = imp.fit_transform(X_trains)
    x_input = X_train.toarray()

    ##    Y_tests = vec.fit_transform(LABELS)
    ##    Y_test=imp.fit_transform(Y_tests)
    ##    y=Y_test.toarray()
    ##    X_value = np.asmatrix(x).astype(np.float)
    ##    Y_value = np.asmatrix(y).astype(np.float)

    X_input_value = np.asmatrix(x_input).astype(np.float)

    ##    train=X_value
    ##    train_labels=Y_value

    test = X_input_value

    ### Initialize our classifier
    ##
    ##    gnb=DecisionTreeClassifier()
    ##
    ##
    ### Train our classifier
    ##    model = gnb.fit(train, train_labels)
    ##
    ##    with open('decision_tree.pickle','wb') as file:
    ##        pickle.dump(gnb,file)
    ##

    pickle_gnb = open(cur_path+'/decision_tree.pickle', 'rb')
    gnb = pickle.load(pickle_gnb)
    preds = gnb.predict(test)
    pred_list = preds.tolist()
    i = pred_list[0]

    for types, value in laba_val.items():
        if value == i:
            QuestionType = types

    return QuestionType


def predict_the_real_question():
    global question

    textWord_Tok_RealQue = []
    # text_Q=Qu.main()
    textWord_Tok_RealQue.append(word_tokenize(question))

    for sen in textWord_Tok_RealQue:
        real_feature_Dict = defaultdict(list)
        real_features_names = PS.ignoring_unwanted_words(sen)
        real_features_name = SC.main(real_features_names)
        coun = 0
        for fea in real_features_name:
            real_feature_Dict[coun] = fea
            coun += 1
    NEWFEATURE.append(real_feature_Dict)

    return real_feature_Dict


def main(questions):
    global question
    question = questions

    textWord_Tok_Data = DSSWL.tokenizing_text_sent_to_word()

    ##    class_classification(textWord_Tok_Data)
    real_feature_Dict = predict_the_real_question()

    the_question_type = data_train()
    if real_feature_Dict[0] == "how":
        if real_feature_Dict[1] == "many":
            the_question_type = "NUM"

    return textWord_Tok_Data, the_question_type, real_feature_Dict
