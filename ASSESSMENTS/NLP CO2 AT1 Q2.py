
words = [
    "unhappy", "redo", "playing", "walked",
    "teacher", "careless", "studies", "cats"
]


prefixes = ["un", "re", "dis", "pre", "mis"]


inflectional_suffixes = ["s", "es", "ed", "ing"]
derivational_suffixes = ["ness", "ment", "er", "or", "less", "ful", "able", "tion", "ity"]


def morphological_parse(word):
    prefix = "-"
    suffix = "-"
    trans_type = "None"
    base = word

   
    for p in prefixes:
        if base.startswith(p):
            prefix = p
            base = base[len(p):]
            trans_type = "Derivational"
            break

    
    for s in sorted(derivational_suffixes, key=len, reverse=True):
        if base.endswith(s):
            suffix = s
            base = base[:-len(s)]
            trans_type = "Derivational"
            break


    if suffix == "-":
        for s in sorted(inflectional_suffixes, key=len, reverse=True):
            if base.endswith(s):
                suffix = s
                base = base[:-len(s)]
                trans_type = "Inflectional"
                break


    if base.endswith("i"):
        base = base[:-1] + "y"      # studies → study
    elif len(base) > 2 and base[-1] == base[-2]:
        base = base[:-1]            # running → run

    return prefix, suffix, trans_type, base


print("-" * 95)
print("{:<12} {:<10} {:<10} {:<18} {:<25} {:<15}".format(
    "Word", "Prefix", "Suffix", "Transformation", "Morphological Breakdown", "Root Word"))
print("-" * 95)

for word in words:
    prefix, suffix, ttype, root = morphological_parse(word)

    breakdown = ""
    if prefix != "-":
        breakdown += prefix + " + "
    breakdown += root
    if suffix != "-":
        breakdown += " + " + suffix

    print("{:<12} {:<10} {:<10} {:<18} {:<25} {:<15}".format(
        word, prefix, suffix, ttype, breakdown, root))

print("-" * 95)
