import AnswerExtract.yesno as yesno
import AnswerExtract.AnswerExtraction as AnswerExtraction


def AnswerExtract(document, qa_details, target):
    #    d = ""
    #    list1 =[]
    #    for li in document:
    #            d = d +" "+ li[0]
    #            list1.append(li[0])

    # Answer yes/no questions

    if qa_details[0] == "Yes/No_Type":
        return yesno.answeryesno(document, target)

    if qa_details[0] == "WH_Type" or qa_details[0] == "List_Type":
        return AnswerExtraction.AnswerExtracter(document, qa_details[1], target)
#        if qa_details[1] == "ABBR":
#            print()
#        if qa_details[1] == "DESC":
#            print()
#        if qa_details[1] == "ENTY":
#            print()
#        if qa_details[1] == "HUM":
#            AnswerExtraction.AnswerExtracter(document,"HUM",target)
#        if qa_details[1] == "NUM":
#            how_many.NumtypeQuestion(document)
#        if qa_details[1] == "LOC":
#            AnswerExtraction.AnswerExtracter(document,"LOC",target)
#        AnswerExtraction.AnswerExtracter(document,type1,target)
