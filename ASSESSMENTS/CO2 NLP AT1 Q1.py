

words = ["playing", "walked", "happiness", "teacher",
         "cats", "running", "careless", "studies"]


inflectional_suffixes = {
    "s", "es", "ed", "ing"
}

derivational_suffixes = {
    "ness", "ment", "er", "or", "ful",
    "less", "able", "ly", "tion", "ity"
}

def morphological_analysis(word):
    suffix = "-"
    suffix_type = "-"
    base = word

   
    for suf in sorted(derivational_suffixes, key=len, reverse=True):
        if word.endswith(suf):
            suffix = suf
            suffix_type = "Derivational"
            base = word[:-len(suf)]
            break

    if suffix == "-":
        for suf in sorted(inflectional_suffixes, key=len, reverse=True):
            if word.endswith(suf):
                suffix = suf
                suffix_type = "Inflectional"
                base = word[:-len(suf)]
                break

    if base.endswith("i"):
        base = base[:-1] + "y"      # studies → study
    elif base.endswith(base[-1] * 2) and len(base) > 2:
        base = base[:-1]            # running → run

    return suffix, suffix_type, base

print("-" * 75)
print("{:<12} {:<20} {:<15} {:<15}".format(
    "Word", "Parsed Structure", "Suffix Type", "Normalized"))
print("-" * 75)

for word in words:
    suffix, suffix_type, base = morphological_analysis(word)

    if suffix != "-":
        parsed = base + " + " + suffix
    else:
        parsed = word

    print("{:<12} {:<20} {:<15} {:<15}".format(
        word, parsed, suffix_type, base))

print("-" * 75)
