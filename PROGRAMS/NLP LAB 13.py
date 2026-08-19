grammar = {
    "S": ["NP", "VP"],
    "NP": ["Det", "N"],
    "VP": ["V", "NP"],
    "Det": ["the"],
    "N": ["cat"],
    "V": ["sees"]
}

def tree(symbol):
    if symbol not in grammar:
        return symbol

    return [symbol] + [tree(x) for x in grammar[symbol]]


parse_tree = tree("S")

print(parse_tree)
