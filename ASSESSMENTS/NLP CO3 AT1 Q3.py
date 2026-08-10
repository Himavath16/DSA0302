from collections import Counter

text = """
the student is learning python
the student is reading books
the student is writing code
the student is studying computer
the teacher is teaching python
the teacher is reading books
the teacher is writing code
the computer is learning python
"""

words = text.lower().split()


unigram = Counter(words)

bigram = Counter(
    (words[i], words[i + 1])
    for i in range(len(words) - 1)
)

trigram = Counter(
    (words[i], words[i + 1], words[i + 2])
    for i in range(len(words) - 2)
)

def P1(word):
    return unigram[word] / len(words)


def P2(w1, w2):
    if unigram[w1] == 0:
        return 0
    return bigram[(w1, w2)] / unigram[w1]


def P3(w1, w2, w3):
    if bigram[(w1, w2)] == 0:
        return 0
    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]


def unsmoothed(w1, w2, word):
    return P3(w1, w2, word)

def backoff(w1, w2, word):

    p = P3(w1, w2, word)

    if p > 0:
        return p, "Trigram"
    p = P2(w2, word)

    if p > 0:
        return p, "Bigram"
    return P1(word), "Unigram"

def interpolation(w1, w2, word):

    lambda1 = 0.2   
    lambda2 = 0.3   
    lambda3 = 0.5   

    return (
        lambda1 * P1(word)
        + lambda2 * P2(w2, word)
        + lambda3 * P3(w1, w2, word)
    )

query = input(
    "Enter an incomplete sentence "
    "(Example: the student is): "
)

q = query.lower().split()

if len(q) < 2:
    print("Please enter at least two words.")

else:

    w1 = q[-2]
    w2 = q[-1]

    print("\nPrevious words:", w1, w2)

    results = []

    for word in unigram:


        p_unsmooth = unsmoothed(w1, w2, word)

        p_backoff, method = backoff(w1, w2, word)

        
        p_interpolation = interpolation(w1, w2, word)

        results.append(
            (
                word,
                p_unsmooth,
                p_backoff,
                method,
                p_interpolation
            )
        )

    unsmooth_best = max(
        results,
        key=lambda x: x[1]
    )

    backoff_best = max(
        results,
        key=lambda x: x[2]
    )

    interpolation_best = max(
        results,
        key=lambda x: x[4]
    )


    print("\n==============================")
    print("PREDICTION RESULTS")
    print("==============================")

    print("\n1. UNSMOOTHED TRIGRAM")
    print(
        "Next word:",
        unsmooth_best[0]
    )
    print(
        "Probability:",
        round(unsmooth_best[1], 4)
    )

    print("\n2. BACKOFF MODEL")
    print(
        "Next word:",
        backoff_best[0]
    )
    print(
        "Probability:",
        round(backoff_best[2], 4)
    )
    print(
        "Used:",
        backoff_best[3]
    )

    print("\n3. DELETED INTERPOLATION")
    print(
        "Next word:",
        interpolation_best[0]
    )
    print(
        "Probability:",
        round(interpolation_best[4], 4)
    )


    print("\n==============================")
    print("ZERO PROBABILITY EXAMPLE")
    print("==============================")

    test_word = "books"

    zero = P3(w1, w2, test_word)

    print(
        "Trigram:",
        "(" + w1, w2, test_word + ")"
    )

    print(
        "Probability:",
        round(zero, 4)
    )

    if zero == 0:
        print(
            "Result: Unseen trigram -> "
            "Zero probability"
        )
