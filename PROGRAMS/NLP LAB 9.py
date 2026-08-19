import re

def pos_tag(sentence):
    words = sentence.split()

    for word in words:
        if re.match(r'^(the|a|an)$', word.lower()):
            tag = "DT"          # Determiner

        elif re.match(r'.*ing$', word.lower()):
            tag = "VBG"         # Verb

        elif re.match(r'.*ly$', word.lower()):
            tag = "RB"          # Adverb

        elif re.match(r'.*ed$', word.lower()):
            tag = "VBD"         # Past tense verb

        elif re.match(r'^[A-Z][a-z]*$', word):
            tag = "NNP"         # Proper noun

        else:
            tag = "NN"          # Noun

        print(word, "->", tag)


sentence = "The boy is running quickly"
pos_tag(sentence)
