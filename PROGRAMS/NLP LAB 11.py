grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"]]
}

def parse(symbol, words, pos=0):
    if symbol not in grammar:
        return pos + 1 if pos < len(words) and words[pos] == symbol else -1

    for rule in grammar[symbol]:
        current = pos
        success = True

        for item in rule:
            current = parse(item, words, current)
            if current == -1:
                success = False
                break

        if success:
            return current

    return -1


sentence = "the cat sees the dog"
words = sentence.split()

result = parse("S", words)

if result == len(words):
    print("Sentence is accepted")
else:
    print("Sentence is rejected")
