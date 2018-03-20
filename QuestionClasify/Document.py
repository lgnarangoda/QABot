import os

def get_Document_Data_Set():
    text_D = []


    cur_path = os.path.dirname(__file__)
    file_Doc = open(cur_path+"/DataFull.txt", mode='r')
    text_D = file_Doc.read()
    return text_D


def main():
    text_D = get_Document_Data_Set()
    return text_D
