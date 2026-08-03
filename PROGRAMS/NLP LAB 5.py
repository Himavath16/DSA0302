

import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt')


stemmer = PorterStemmer()


words = [
    "running", "playing", "studies", "happiness",
    "fishing", "connected", "wolves", "better"
]

print("{:<15} {:<15}".format("Original Word", "Stemmed Word"))
print("-" * 30)


for word in words:
    stem = stemmer.stem(word)
    print("{:<15} {:<15}".format(word, stem))
