import re
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
import QuestionClasify.DocumentWordList as DWL
import os
textSent_Tok_Que = DWL.main()


def words(text): return re.findall(r'\w+', text.lower())

cur_path = os.path.dirname(__file__)
WORDS = Counter(words(open(cur_path+"/DataFull.txt", encoding="utf8").read()))


def P(word, N=sum(WORDS.values())):
    return WORDS[word] / N


def correction(word):
    return max(candidates(word), key=P)


def candidates(word):
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


def known(words):
    return set(w for w in words if w in WORDS)


def edits1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


def main(text):
    new_sentence = []
    for te in text:
        if te not in textSent_Tok_Que:
            new_sentence.append(correction(te))

        else:
            new_sentence.append(te)

    return new_sentence
