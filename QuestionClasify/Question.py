def get_the_Question():
    text_Q = []

    file_Q = open("D:\ifs final\git\code\QuestionClasify/RealQue.txt", mode='r')
    text_Q = file_Q.read()

    return text_Q


def main():
    text_Q = get_the_Question()
    return text_Q
