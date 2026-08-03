

import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = ["running", "studies", "better", "playing", "wolves"]

print("Morphological Analysis:\n")

for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)

    print("Original Word :", word)
    print("Stem          :", stem)
    print("Lemma         :", lemma)
    print()
