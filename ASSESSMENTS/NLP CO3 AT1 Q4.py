from collections import Counter
import math
train = "the student is learning python the student is reading books the teacher is learning python"
tests = [
    "the student is learning",
    "the teacher is learning",
    "the student is playing"
]

words = train.split()
V = len(set(words))
uni = Counter(words)
bi = Counter(zip(words, words[1:]))
tri = Counter(zip(words, words[1:], words[2:]))
def U(w):
    return uni[w] / len(words)

def B(a, b):
    return bi[(a, b)] / uni[a] if uni[a] else 0

def T(a, b, c):
    return tri[(a, b, c)] / bi[(a, b)] if bi[(a, b)] else 0
def entropy(sentence, n, smooth=False):
    w = sentence.split()
    total = 0
    count = 0

    for i in range(n - 1, len(w)):

        if n == 1:
            p = (uni[w[i]] + 1) / (len(words) + V) if smooth else U(w[i])

        elif n == 2:
            p = ((bi[(w[i-1], w[i])] + 1) /
                 (uni[w[i-1]] + V)) if smooth else B(w[i-1], w[i])

        else:
            p = ((tri[(w[i-2], w[i-1], w[i])] + 1) /
                 (bi[(w[i-2], w[i-1])] + V)) if smooth else T(w[i-2], w[i-1], w[i])

        if p > 0:
            total += -math.log2(p)
            count += 1

    return total / count if count else 0
for sentence in tests:
    print("\nSentence:", sentence)

    print("Unigram :", round(entropy(sentence, 1), 2))
    print("Bigram  :", round(entropy(sentence, 2), 2))
    print("Trigram :", round(entropy(sentence, 3), 2))

    print("Smoothed Trigram:",
          round(entropy(sentence, 3, True), 2))

print("\nLow entropy  = More predictable")
print("High entropy = Less predictable")
