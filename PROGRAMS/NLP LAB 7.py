import nltk
from nltk import word_tokenize, pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "The quick brown fox jumps over the lazy dog."

words = word_tokenize(text)

tagged_words = pos_tag(words)

print("{:<15} {:<15}".format("Word", "POS Tag"))
print("-" * 30)

for word, tag in tagged_words:
    print("{:<15} {:<15}".format(word, tag))
