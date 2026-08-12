sentence1 = "Book a flight ticket now"
sentence2 = "This book is interesting"


def pos_tag(sentence):
    words = sentence.split()
    tagged_words = []

    for i, word in enumerate(words):
        word_lower = word.lower()

        # Rules for the word "book"
        if word_lower == "book":
            if i == 0:
                tag = "VB"       # Verb at beginning
            else:
                tag = "NN"       # Noun after determiner

        elif word_lower in ["a", "an", "the", "this", "that"]:
            tag = "DT"

        elif word_lower in ["flight", "ticket"]:
            tag = "NN"

        elif word_lower == "is":
            tag = "VBZ"

        elif word_lower == "interesting":
            tag = "JJ"

        elif word_lower == "now":
            tag = "RB"

        else:
            tag = "NN"

        tagged_words.append((word, tag))

    return tagged_words


print("=" * 50)
print("RULE-BASED POS TAGGING")
print("=" * 50)

result1 = pos_tag(sentence1)
result2 = pos_tag(sentence2)

print("\nSentence 1:")
for word, tag in result1:
    print(word, "->", tag)

print("\nSentence 2:")
for word, tag in result2:
    print(word, "->", tag)

# Given probabilities
P_book_VB = 0.6
P_book_NN = 0.4

P_start_VB = 0.5
P_start_NN = 0.5


# Calculate probability of book being VB
prob_VB = P_start_VB * P_book_VB

# Calculate probability of book being NN
prob_NN = P_start_NN * P_book_NN


print("\n" + "=" * 50)
print("HMM PROBABILITY")
print("=" * 50)

print("\nP(Start -> VB) =", P_start_VB)
print("P(book | VB) =", P_book_VB)

print("\nP(book is VB) =")
print(P_start_VB, "*", P_book_VB)

print("=", prob_VB)


print("\nP(Start -> NN) =", P_start_NN)
print("P(book | NN) =", P_book_NN)

print("\nP(book is NN) =")
print(P_start_NN, "*", P_book_NN)

print("=", prob_NN)

print("\n" + "=" * 50)
print("HMM DECISION")
print("=" * 50)

if prob_VB > prob_NN:
    print("\n'Book' is predicted as: VB (Verb)")
else:
    print("\n'Book' is predicted as: NN (Noun)")



print("\n" + "=" * 50)
print("FINAL RESULTS")
print("=" * 50)

print("\nSentence 1:")
print("Book/VB a/DT flight/NN ticket/NN now/RB")

print("\nSentence 2:")
print("This/DT book/NN is/VBZ interesting/JJ")

print("\nHMM Probability:")
print("P(VB, book) =", prob_VB)
print("P(NN, book) =", prob_NN)

print("\nFinal HMM Tag for 'Book': VB")
