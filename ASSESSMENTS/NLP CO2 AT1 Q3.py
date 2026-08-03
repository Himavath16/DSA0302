# Stemming-Based Preprocessing Module for a Search Engine

from nltk.stem import PorterStemmer


stemmer = PorterStemmer()

words = ["played", "player", "playing"]


inflectional_suffixes = ["ed", "ing", "s", "es"]
derivational_suffixes = ["er", "or", "ness", "ment", "less", "ful", "able", "tion", "ity"]

print("-" * 95)
print("{:<12} {:<12} {:<15} {:<18} {:<20}".format(
    "Original", "Stem", "Removed Affix", "Transformation", "Normalized Form"))
print("-" * 95)

for word in words:
    stem = stemmer.stem(word)

    removed_affix = "-"
    transformation = "None"

    
    for suffix in sorted(inflectional_suffixes + derivational_suffixes,
                         key=len, reverse=True):
        if word.endswith(suffix):
            removed_affix = suffix
            if suffix in inflectional_suffixes:
                transformation = "Inflectional"
            else:
                transformation = "Derivational"
            break


    normalized = stem

    print("{:<12} {:<12} {:<15} {:<18} {:<20}".format(
        word, stem, removed_affix, transformation, normalized))

print("-" * 95)
