

import math

# Sentence
words = [
    "economic",
    "growth",
    "increases",
    "employment"
]

# Initial POS tags
tags = [
    "JJ",
    "NN",
    "NNS",
    "NN"
]



print("Initial POS Tags:")
for word, tag in zip(words, tags):
    print(word, "/", tag)

for i in range(1, len(tags)):

    if tags[i] == "NNS" and tags[i - 1] == "NN":
        tags[i] = "VBZ"


print("\nCorrected POS Tags:")
for word, tag in zip(words, tags):
    print(word, "/", tag)



frequency = {
    "economic": 120,
    "growth": 450,
    "increases": 210,
    "employment": 380
}

total = sum(frequency.values())

print("\nWord Frequency Distribution:")

for word, count in frequency.items():

    probability = count / total

    print(
        word,
        "Frequency =", count,
        "Probability =", round(probability, 4)
    )

p_nns = 0.5
p_vbz = 0.5

entropy_before = -(
    p_nns * math.log2(p_nns) +
    p_vbz * math.log2(p_vbz)
)



p_nns = 0.1
p_vbz = 0.9

entropy_after = -(
    p_nns * math.log2(p_nns) +
    p_vbz * math.log2(p_vbz)
)


print("\nEntropy Analysis")

print(
    "Entropy before transformation =",
    round(entropy_before, 4),
    "bits"
)

print(
    "Entropy after transformation =",
    round(entropy_after, 4),
    "bits"
)
