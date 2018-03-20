questionwords = ["who", "what", "where", "when", "why", "how", "whose", "which", "whom"]
yesnowords = ["can", "could", "would", "is", "does", "has", "was", "were", "had", "have", "did", "are", "will"]


def target_identifying(qwords):
    # Find "question word" (what, who, where, etc.)
    questionword = ""
    qid = -1

    for (idx, word) in enumerate(qwords):
        if word.lower() in questionwords:
            questionword = word.lower()
            qid = idx  # 0
            break
        elif word.lower() in yesnowords:
            return (qwords)
    if qid < 0:
        return (qwords)
    if qid > len(qwords) - 3:
        target = qwords[:qid]
    else:
        target = qwords[qid + 1:]

    # Determine question type
    if questionword == "how":
        if target[0] in ["few", "little", "much", "many"]:
            target = target[1:]
        elif target[0] in ["young", "old", "long"]:
            target = target[1:]

    # Trim possible extra helper verb
    if questionword == "which":
        target = target[1:]
    if target[0] in yesnowords:
        target = target[1:]

    # Return question data
    return target
