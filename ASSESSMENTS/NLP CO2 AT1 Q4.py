# Finite-State Morphological Parser for English Verb Forms

# Input words
words = ["writes", "writing", "written"]

# Finite-State Morphological Parser
def morphological_parser(word):
    transitions = ["q0(Start)"]
    root = ""
    suffix = ""
    inflection = ""
    normalized = ""


    irregular = {
        "written": ("write", "en", "Irregular Inflection")
    }

 
    if word in irregular:
        root, suffix, inflection = irregular[word]
        transitions.extend([
            "q1(Check Irregular)",
            "q2(Irregular Match)",
            "qF(Accept)"
        ])

    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        inflection = "Regular Inflection"

       
        if root.endswith("writ"):
            root = "write"

        transitions.extend([
            "q1(Read Stem)",
            "q2(Read Suffix -ing)",
            "qF(Accept)"
        ])

    elif word.endswith("es"):
        root = word[:-2]
        suffix = "es"
        inflection = "Regular Inflection"

        transitions.extend([
            "q1(Read Stem)",
            "q2(Read Suffix -es)",
            "qF(Accept)"
        ])

    elif word.endswith("s"):
        root = word[:-1]
        suffix = "s"
        inflection = "Regular Inflection"

        transitions.extend([
            "q1(Read Stem)",
            "q2(Read Suffix -s)",
            "qF(Accept)"
        ])

    else:
        root = word
        suffix = "-"
        inflection = "Base Form"

        transitions.extend([
            "q1(Base Word)",
            "qF(Accept)"
        ])

    normalized = root

    return {
        "word": word,
        "root": root,
        "suffix": suffix,
        "type": inflection,
        "path": " → ".join(transitions),
        "normalized": normalized
    }


print("=" * 120)
print("{:<10} {:<12} {:<10} {:<22} {:<45} {:<12}".format(
    "Word", "Root", "Suffix", "Inflection Type",
    "State Transition Path", "Normalized"))
print("=" * 120)

for word in words:
    result = morphological_parser(word)

    print("{:<10} {:<12} {:<10} {:<22} {:<45} {:<12}".format(
        result["word"],
        result["root"],
        result["suffix"],
        result["type"],
        result["path"],
        result["normalized"]
    ))

print("=" * 120)
