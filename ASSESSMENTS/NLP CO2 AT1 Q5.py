

from nltk.stem import PorterStemmer


stemmer = PorterStemmer()

words = ["relational", "relation", "relate"]

def porter_stemming_steps(word):
    steps = []
    current = word
    rules = []

    
    if current.endswith("ational"):
        current = current.replace("ational", "ate")
        rules.append("ational → ate")
        steps.append(current)

    if current.endswith("tional"):
        current = current.replace("tional", "tion")
        rules.append("tional → tion")
        steps.append(current)


    if current.endswith("ation"):
        current = current.replace("ation", "ate")
        rules.append("ation → ate")
        steps.append(current)

    
    if current.endswith("e") and len(current) > 3:
        current = current[:-1]
        rules.append("remove final e")
        steps.append(current)

    final_stem = stemmer.stem(word)

    return rules, steps, final_stem


print("=" * 100)
print("{:<12} {:<25} {:<35} {:<15}".format(
    "Word", "Applied Rules", "Intermediate Forms", "Final Stem"))
print("=" * 100)

for word in words:
    rules, forms, stem = porter_stemming_steps(word)

    print("{:<12} {:<25} {:<35} {:<15}".format(
        word,
        ", ".join(rules) if rules else "No rule",
        " → ".join(forms) if forms else word,
        stem
    ))

print("=" * 100)
