import string
import random

# Create Unigrams
def create_unigrams(words):
    counts = dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

# Prints the Unigrams
def show_unigrams(unigrams):
    print("Unigrams:")
    print(unigrams)

# Create Bigrams
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

# Prints Bigrams
def show_bigrams(bigrams):
    print("")
    print("Bigrams:")
    print(bigrams)

# Generates 4 random words from the corps and then shows the probability of that sentence
def generate_random(unigrams, bigrams):
    word1 = list(unigrams)[random.randint(0, len(unigrams)-1)]
    word2 = list(unigrams)[random.randint(0, len(unigrams)-1)]
    word3 = list(unigrams)[random.randint(0, len(unigrams)-1)]
    word4 = list(unigrams)[random.randint(0, len(unigrams)-1)]
    show_result(word1, word2, word3, word4, bigrams)

# Computes the probability of the sentence including 4 words using bigrams
def show_result(word1, word2, word3, word4, bigrams):
    print("")
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
    


# Our mini corps
text = "It was the season of sales. The august establishment of Walpurgis and Nettlepink had lowered its prices for an entire week as a concession to trade observances, much as an Arch-duchess might protestingly contract an attack of influenza for the unsatisfactory reason that influenza was locally prevalent. Adela Chemping, who considered herself in some measure superior to the allurements of an ordinary bargain sale, made a point of attending the reduction week at Walpurgis and Nettlepink's."

# Extracting words of the mini corps
words = [word.strip(string.punctuation) for word in text.split()]
words = [word.lower() for word in words]

# Creating and displaying unigrams using the words of the corps
unigrams = create_unigrams(words)
show_unigrams(unigrams)

# Creating and displaying bigrams using unigrams
bigrams = create_bigrams(unigrams)
show_bigrams(bigrams)

# Generating a random sentence and displaying the probability
generate_random(unigrams, bigrams)