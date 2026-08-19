grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"]]
}

def earley_parse(words):
    chart = [[] for _ in range(len(words) + 1)]

    chart[0].append(("S", ["NP", "VP"], 0, 0))

    for i in range(len(words) + 1):
        changed = True

        while changed:
            changed = False

            for lhs, rhs, dot, start in chart[i]:
                if dot < len(rhs):
                    symbol = rhs[dot]

                    
                    if symbol in grammar:
                        for rule in grammar[symbol]:
                            item = (symbol, rule, 0, i)
                            if item not in chart[i]:
                                chart[i].append(item)
                                changed = True

                    
                    elif i < len(words) and symbol == words[i]:
                        item = (lhs, rhs, dot + 1, start)
                        if item not in chart[i + 1]:
                            chart[i + 1].append(item)

                else:
                    
                    for l, r, d, s in chart[start]:
                        if d < len(r) and r[d] == lhs:
                            item = (l, r, d + 1, s)
                            if item not in chart[i]:
                                chart[i].append(item)
                                changed = True

    final = ("S", ["NP", "VP"], 2, 0)

    return final in chart[len(words)]


sentence = "the cat sees the dog"
words = sentence.split()

if earley_parse(words):
    print("Sentence accepted")
else:
    print("Sentence rejected")
