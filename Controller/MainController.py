import nltk

# import datetime
# a = datetime.datetime.now()
# b = datetime.datetime.now()
# print("QA time - ",b-a)

question = "question"
target = []
file_name = "filename"
Document = ""
qa_details = ""
answer = "answer"
import nltk
nltk.download('punkt')

import nltk
nltk.download('averaged_perceptron_tagger')
import nltk
nltk.download('wordnet')

def set_filename_and_question(filename, questions):
    global file_name
    file_name = filename
    global question
    question = questions
    get_target()
    qa_clasify()
    dc()
    get_answer()
    return answer
    # //return "answer from main"


def get_target():
    global question
    question1 = question.replace('?', '')
    question1 = nltk.word_tokenize(question1)
    global target
    import QuestionClasify.TargetIdentifier as TargetIdentifier
    target = TargetIdentifier.target_identifying(question1)
    print(target)
    return 0


def qa_clasify():
    global qa_details
    import Controller.ControllerQueClassify as ControllerQueClassify
    qa_details = ControllerQueClassify.get(question)
    type1 = qa_details[1]
    print(qa_details)
    return 0


def dc():
    global Document
    import Controller.DpController as DpController
    Document = DpController.DocumentProcess(target, file_name)
    print(Document)
    return 0


def get_answer():
    global answer
    import Controller.AnswerController as AnswerController
    answer = AnswerController.AnswerExtract(Document, qa_details, target)
    print(answer)
    return 0


print(answer)

print(file_name)
