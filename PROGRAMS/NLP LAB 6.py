import random


text = """
the cat sat on the mat
the cat ate the fish
the dog sat on the rug
the dog chased the cat
"""


words = text.split()


bigram = {}

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]

    if current_word not in bigram:
        bigram[current_word] = []

    bigram[current_word].append(next_word)

def generate_text(start_word, length):
    word = start_word
    sentence = [word]

    for _ in range(length - 1):
        if word in bigram:
            word = random.choice(bigram[word])
            sentence.append(word)
        else:
            break

    return " ".join(sentence)

start = "the"
generated = generate_text(start, 10)

print("Generated Text:")
print(generated)
