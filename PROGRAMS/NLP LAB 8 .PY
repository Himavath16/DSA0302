
training = {
    "The": "DT",
    "cat": "NN",
    "dog": "NN",
    "runs": "VB",
    "eats": "VB",
    "a": "DT"
}

sentence = "The cat runs"

words = sentence.split()

for word in words:
    if word in training:
        print(word, "->", training[word])
    else:
        print(word, "->", "NN")
