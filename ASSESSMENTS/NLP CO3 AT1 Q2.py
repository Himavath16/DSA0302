from collections import Counter
text = """
the student is learning python
the student is reading books
the student is writing code
the teacher is teaching python
the teacher is reading books
the teacher is writing code
"""
words = text.lower().split()

words = ["<s>", "<s>"] + words + ["</s>"]

unigram = Counter(words)

bigram = Counter(
    (words[i], words[i+1])
    for i in range(len(words)-1)
)

trigram = Counter(
    (words[i], words[i+1], words[i+2])
    for i in range(len(words)-2)
)

def unigram_prob(w):
    return unigram[w] / len(words)


def bigram_prob(w1, w2):
    if unigram[w1] == 0:
        return 0
    return bigram[(w1, w2)] / unigram[w1]


def trigram_prob(w1, w2, w3):
    if bigram[(w1, w2)] == 0:
        return 0
    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]

def unsmoothed(w1, w2, w3):
    return trigram_prob(w1, w2, w3)

def backoff(w1, w2, w3):

    p = trigram_prob(w1, w2, w3)

    if p > 0:
        return p, "Trigram"

    p = bigram_prob(w2, w3)

    if p > 0:
        return p, "Bigram"

    return unigram_prob(w3), "Unigram"
def interpolation(w1, w2, w3):

    
    l1 = 0.2
    l2 = 0.3
    l3 = 0.5

    p1 = unigram_prob(w3)
    p2 = bigram_prob(w2, w3)
    p3 = trigram_prob(w1, w2, w3)

    return l1*p1 + l2*p2 + l3*p3


sentence = "the student is"
s = sentence.split()

w1 = s[-2]
w2 = s[-1]

print("INPUT SENTENCE:", sentence)

print("\nMODEL COMPARISON")
print("=" * 50)

results = []

for word in unigram:

    if word in ["<s>", "</s>"]:
        continue

    p1 = unsmoothed(w1, w2, word)

    p2, method = backoff(w1, w2, word)

    p3 = interpolation(w1, w2, word)

    results.append((word, p1, p2, method, p3))


# Sort by probability
unsmooth_top = sorted(
    results,
    key=lambda x: x[1],
    reverse=True
)[:5]

backoff_top = sorted(
    results,
    key=lambda x: x[2],
    reverse=True
)[:5]

interpolation_top = sorted(
    results,
    key=lambda x: x[4],
    reverse=True
)[:5]




print("\nUNSMOOTHED MODEL")
for word, p, _, _, _ in unsmooth_top:
    print(word, "->", round(p, 3))


print("\nBACKOFF MODEL")
for word, _, p, method, _ in backoff_top:
    print(word, "->", round(p, 3), "(" + method + ")")


print("\nDELETED INTERPOLATION")
for word, _, _, _, p in interpolation_top:
    print(word, "->", round(p, 3))




print("\nZERO PROBABILITY EXAMPLE")
print("=" * 50)

test_word = "books"

p = unsmoothed("the", "student", test_word)

print(
    "P(books | the student) =",
    p
)

if p == 0:
    print("Trigram is unseen -> Probability is ZERO")


print("\nBACKOFF EXAMPLE")
print("=" * 50)

p, method = backoff("the", "student", "books")

print(
    "P(books | the student) =",
    round(p, 3)
)

print("Used:", method)
