import string
import random

def create_unigrams(words):
    counts = dict()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def show_unigrams(unigrams):
    print(unigrams)


def create_bigrams(unigrams):
    bigrams = dict()
    for word in unigrams:
        for word2 in unigrams:
            mykey = word2 + "|" + word
            if mykey not in bigrams:
                counter = 0
                for i in range(0, len(words)-1):
                    if words[i] == word and words[i+1] == word2:
                        counter += 1

                bigrams[mykey] = float(counter/unigrams[word])
    return bigrams


def show_bigrams(bigrams):
    print(bigrams)


def generate_random(unigrams, bigrams):
    word1 = list(unigrams)[random.randint(0, len(unigrams)-1)]
    word2 = list(unigrams)[random.randint(0, len(unigrams)-1)]
    word3 = list(unigrams)[random.randint(0, len(unigrams)-1)]
    word4 = list(unigrams)[random.randint(0, len(unigrams)-1)]
    show_result(word1, word2, word3, word4, bigrams)


def show_result(word1, word2, word3, word4, bigrams):
    print("P(" + word1 + " " + word2 + " " + word3 + " " + word4 + ") = P(" + 
        word2 + "|" + word1 + ") * P(" + 
        word3 + "|" + word2 + ") * P(" +
        word4 + "|" + word3 + ")")

    print(" = ", end="")
    print(bigrams[word2 + "|" + word1], end="")
    print(" * ", end="")
    print(bigrams[word3 + "|" + word2], end="")
    print(" * ", end="")
    print(bigrams[word4 + "|" + word3], end="")
    print(" = ", end="")
      
    print(bigrams[word2 + "|" + word1]*bigrams[word3 + "|" + word2]*bigrams[word4 + "|" + word3])
    



text = "folan, kar test konim! Konim."
words = [word.strip(string.punctuation) for word in text.split()]
words = [word.lower() for word in words]

unigrams = create_unigrams(words)
show_unigrams(unigrams)



bigrams = create_bigrams(unigrams)

show_bigrams(bigrams)


