import QuestionClasify.Version0401 as Ver01
import QuestionClasify.Version0402 as Ver02
import QuestionClasify.Version0403 as Ver03
import pickle


def get(question):
    textWord_Tok_Data, maintextType, real_feature_Dict = Ver01.main(question)

    main_type = Ver03.main(question)
    subtextType = Ver02.main(textWord_Tok_Data, real_feature_Dict, maintextType)

    return main_type, maintextType, subtextType, list(real_feature_Dict.values())
