from nltk.tokenize import sent_tokenize, word_tokenize
import pandas
import nltk
from collections import defaultdict
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.preprocessing import Imputer
from sklearn import svm
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import CountVectorizer
import pickle
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
import os
cur_path = os.path.dirname(__file__)
import QuestionClasify.PolishSentence as PS

subFEATURES = []
subLABELS = []
NEWsubFEATURE = []
text_sub_type = defaultdict(list)
text_sub_type_dict = defaultdict(list)


def create_text_sub_type_dict(textWord_Tok_Que, textType):
    for sen in textWord_Tok_Que:
        if sen[0] == textType:
            text_sub_type[sen[2]].append(sen[3:])

    counter = 1
    for sub in list(text_sub_type.keys()):
        text_sub_type_dict[sub] = counter
        counter += 1


def get_K_Value(labeltype):
    for nv in text_sub_type_dict:
        if labeltype == nv:
            k = text_sub_type_dict[nv]
            return k


def subclass_classification(textWord_Tok_Que, textType):
    for sen in textWord_Tok_Que:
        if sen[0] == textType:
            feature_Dict = defaultdict(list)
            label_Dict = defaultdict(list)
            laba_val_num = get_K_Value(sen[2])
            label_Dict['key'] = laba_val_num

            features_name = PS.ignoring_unwanted_words(sen[3:])
            coun = 0
            for fea in features_name:
                feature_Dict[coun] = fea
                coun += 1
            subFEATURES.append(feature_Dict)
            subLABELS.append(label_Dict)


def data_train():
    ##    vec=DictVectorizer()
    imp = Imputer(missing_values='NaN', strategy='median', axis=0)

    ##
    ##    X_tests = vec.fit_transform(subFEATURES)
    ##    X_test=imp.fit_transform(X_tests)
    ##    x=X_test.toarray()
    ##
    ##    with open('data_train01.pickle','wb') as ff:
    ##        pickle.dump(vec,ff)

    pickle_vec = open(cur_path+'/data_train01.pickle', 'rb')
    vec = pickle.load(pickle_vec)

    X_trains = vec.transform(NEWsubFEATURE)
    X_train = imp.fit_transform(X_trains)
    x_input = X_train.toarray()

    ##    Y_tests = vec.fit_transform(subLABELS)
    ##    Y_test=imp.fit_transform(Y_tests)
    ##    y=Y_test.toarray()
    ##    X_value = np.asmatrix(x).astype(np.float)
    ##    Y_value = np.asmatrix(y).astype(np.float)

    X_input_value = np.asmatrix(x_input).astype(np.float)

    ##    train=X_value
    ##    train_labels=Y_value
    test = X_input_value

    ### Initialize our classifier
    ##    #gnb = GaussianNB()
    ##    #gnb=svm.SVC()
    ##    #gnb=MultinomialNB()
    ##    #gnb=RandomForestClassifier()
    ##    #gnb=ExtraTreesClassifier()
    ##    gnb=DecisionTreeClassifier()
    ##    #gnb=AdaBoostClassifier()
    ##    #gnb=GradientBoostingClassifier()
    ##
    ##
    ### Train our classifier
    ##    model = gnb.fit(train, train_labels)
    ##
    ##    with open('decision_tree01.pickle','wb') as file:
    ##        pickle.dump(gnb,file)

    pickle_gnb = open(cur_path+'/decision_tree01.pickle', 'rb')
    gnb = pickle.load(pickle_gnb)

    preds = gnb.predict(test)
    pred_list = preds.tolist()
    i = pred_list[0]

    for types, value in text_sub_type_dict.items():
        if value == i:
            subtextType = types

    return subtextType


def main(textWord_Tok_Que, real_feature_dic, textType):
    create_text_sub_type_dict(textWord_Tok_Que, textType)

    subclass_classification(textWord_Tok_Que, textType)
    NEWsubFEATURE.append(real_feature_dic)
    subtextType = data_train()

    return subtextType
