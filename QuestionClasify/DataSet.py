import os


def get_Data_Set():
    text_DS = []
    cur_path = os.path.dirname(__file__)
    file_DS = open(cur_path+"/DataFull.txt", mode='r',encoding = "ISO-8859-1")
    text_DS = file_DS.read()
    return text_DS
