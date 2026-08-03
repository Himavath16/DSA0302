

def generate_plural(noun):
    
    if noun.endswith(("s", "x", "z", "ch", "sh")):
        # State 1: Add "es"
        plural = noun + "es"

    elif noun.endswith("y") and len(noun) > 1 and noun[-2].lower() not in "aeiou":
        # State 2: Replace 'y' with 'ies'
        plural = noun[:-1] + "ies"

    else:
        # State 3: Add "s"
        plural = noun + "s"

    return plural


nouns = [
    "cat", "dog", "bus", "box",
    "church", "dish", "baby", "city", "toy"
]

print("{:<12} {:<12}".format("Singular", "Plural"))
print("-" * 25)

for noun in nouns:
    print("{:<12} {:<12}".format(noun, generate_plural(noun)))
