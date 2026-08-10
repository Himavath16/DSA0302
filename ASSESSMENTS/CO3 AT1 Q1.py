from collections import Counter

text = """
the student is learning python
the student is reading books
the student is writing code
the teacher is teaching python
the teacher is reading books
"""

words = text.lower().split()

def ngrams(n):
    return Counter(
        tuple(words[i:i+n])
        for i in range(len(words)-n+1)
    )

n = int(input("Enter N (1, 2 or 3): "))

counts = ngrams(n)

print("\nN-Gram Counts:")
for gram, count in counts.items():
    print(gram, ":", count)

sentence = input("\nEnter sentence: ").lower().split()

if n == 1:
    context = ()
else:
    context = tuple(sentence[-(n-1):])

predictions = []

for gram, count in counts.items():
    if n == 1 or gram[:-1] == context:
        predictions.append((gram[-1], count))

predictions.sort(key=lambda x: x[1], reverse=True)

print("\nTop-5 Next Words:")
for word, count in predictions[:5]:
    print(word, "->", count)

print("\nUnseen N-Gram Probability: 0")
