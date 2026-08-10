from collections import Counter
text = """
the student is learning python
the student is reading books
the student is writing code
the teacher is teaching python
the teacher is reading books
"""

words = text.lower().split()

def make_ngrams(n):
    return Counter(
        tuple(words[i:i+n])
        for i in range(len(words) - n + 1)
    )


for n in [1, 2, 3]:

    print("\n", n, "-GRAM")
    print("=" * 30)

    counts = make_ngrams(n)

    for gram, count in counts.items():
        print(gram, ":", count)


sentence = "the student is"
context = tuple(sentence.split()[-1:])

counts = make_ngrams(2)

predictions = []

for gram, count in counts.items():

    if gram[:-1] == context:
        predictions.append((gram[-1], count))

predictions.sort(key=lambda x: x[1], reverse=True)

print("\nNEXT WORD PREDICTION")
print("=" * 30)

print("Sentence:", sentence)

for word, count in predictions[:5]:
    print(word, "-> Count:", count)


print("\nBIGRAM PROBABILITIES")
print("=" * 30)

total = sum(counts[g] for g in counts if g[0] == "is")

for gram, count in counts.items():

    if gram[0] == "is":
        probability = count / total
        print(
            gram,
            "->",
            round(probability, 2)
        )


print("\nUNSEEN N-GRAM")
print("=" * 30)

unseen = ("student", "plays")

print(
    unseen,
    "-> Probability: 0"
)
