import math
from collections import Counter


corpus = """
data science is powerful
data science drives innovation
data science is evolving
"""

# Tokenize the corpus
words = corpus.lower().split()

print("=" * 60)
print("SMART MOBILE KEYBOARD PREDICTION SYSTEM")
print("=" * 60)

print("\nTraining Corpus:")
print(words)

print("\nTotal number of words:", len(words))

# Unigram counts
unigram_counts = Counter(words)

# Bigram counts
bigram_counts = Counter(
    (words[i], words[i + 1])
    for i in range(len(words) - 1)
)

# Trigram counts
trigram_counts = Counter(
    (words[i], words[i + 1], words[i + 2])
    for i in range(len(words) - 2)
)


print("\n" + "=" * 60)
print("N-GRAM COUNTS")
print("=" * 60)

print("\nUnigram Counts:")
for word, count in unigram_counts.items():
    print(f"{word}: {count}")

print("\nBigram Counts:")
for bigram, count in bigram_counts.items():
    print(f"{bigram}: {count}")

print("\nTrigram Counts:")
for trigram, count in trigram_counts.items():
    print(f"{trigram}: {count}")


def bigram_probability(word1, word2):
    """
    Calculate:
        P(word2 | word1)
    using Maximum Likelihood Estimation.
    """

    numerator = bigram_counts[(word1, word2)]
    denominator = unigram_counts[word1]

    if denominator == 0:
        return 0

    return numerator / denominator


p_science_given_data = bigram_probability("data", "science")


print("\n" + "=" * 60)
print("1. MLE BIGRAM PROBABILITY")
print("=" * 60)

print("\nC(data) =", unigram_counts["data"])
print("C(data science) =", bigram_counts[("data", "science")])

print("\nP(science | data) = C(data science) / C(data)")

print(
    f"P(science | data) = "
    f"{bigram_counts[('data', 'science')]} / "
    f"{unigram_counts['data']}"
)

print(f"\nP(science | data) = {p_science_given_data:.4f}")



def trigram_probability(word1, word2, word3):
    """
    Calculate:
        P(word3 | word1, word2)
    """

    numerator = trigram_counts[(word1, word2, word3)]
    denominator = bigram_counts[(word1, word2)]

    if denominator == 0:
        return 0

    return numerator / denominator


p_is_trigram = trigram_probability(
    "data",
    "science",
    "is"
)


print("\n" + "=" * 60)
print("TRIGRAM PROBABILITY")
print("=" * 60)

print("\nC(data science) =",
      bigram_counts[("data", "science")])

print("C(data science is) =",
      trigram_counts[("data", "science", "is")])

print("\nP(is | data, science) = "
      "C(data science is) / C(data science)")

print(
    f"\nP(is | data, science) = "
    f"{trigram_counts[('data', 'science', 'is')]} / "
    f"{bigram_counts[('data', 'science')]}"
)

print(f"\nTrigram Probability = {p_is_trigram:.4f}")



p_is_bigram = bigram_probability("science", "is")

print("\n" + "=" * 60)
print("BIGRAM PROBABILITY")
print("=" * 60)

print("\nC(science) =",
      unigram_counts["science"])

print("C(science is) =",
      bigram_counts[("science", "is")])

print(f"\nP(is | science) = {p_is_bigram:.4f}")



def unigram_probability(word):
    """
    Calculate:
        P(word)
    """

    total_words = len(words)

    return unigram_counts[word] / total_words


p_is_unigram = unigram_probability("is")


print("\n" + "=" * 60)
print("UNIGRAM PROBABILITY")
print("=" * 60)

print("\nC(is) =", unigram_counts["is"])
print("Total words =", len(words))

print(
    f"\nP(is) = {unigram_counts['is']} / {len(words)}"
)

print(f"\nP(is) = {p_is_unigram:.4f}")


# ------------------------------------------------------------
# 7. BACKOFF MODEL
# Sequence: data science improves
# ------------------------------------------------------------

def backoff_probability(word1, word2, word3):
    """
    Backoff strategy:

    1. Try trigram
    2. If unavailable, try bigram
    3. If unavailable, try unigram
    4. If word is completely unseen, return 0
    """

    # Try trigram
    trigram_count = trigram_counts[(word1, word2, word3)]

    if trigram_count > 0:
        probability = trigram_probability(
            word1,
            word2,
            word3
        )

        return probability, "Trigram"

    # Try bigram
    bigram_count = bigram_counts[(word2, word3)]

    if bigram_count > 0:
        probability = bigram_probability(
            word2,
            word3
        )

        return probability, "Bigram"

    # Try unigram
    unigram_count = unigram_counts[word3]

    if unigram_count > 0:
        probability = unigram_probability(word3)

        return probability, "Unigram"

    # Completely unseen
    return 0, "No available n-gram"


backoff_prob, backoff_level = backoff_probability(
    "data",
    "science",
    "improves"
)


print("\n" + "=" * 60)
print("2. BACKOFF MODEL")
print("=" * 60)

print("\nSequence: data science improves")

print("\nTrying Trigram:")
print("P(improves | data, science) = 0")

print("\nTrying Bigram:")
print("P(improves | science) = 0")

print("\nTrying Unigram:")
print("P(improves) = 0")

print("\nBackoff Level:", backoff_level)
print(f"Backoff Probability = {backoff_prob:.4f}")


# ------------------------------------------------------------
# 8. DELETED INTERPOLATION
# ------------------------------------------------------------

lambda1 = 0.5  # Trigram
lambda2 = 0.3  # Bigram
lambda3 = 0.2  # Unigram


interpolated_probability = (
    lambda1 * p_is_trigram
    + lambda2 * p_is_bigram
    + lambda3 * p_is_unigram
)


print("\n" + "=" * 60)
print("3. DELETED INTERPOLATION")
print("=" * 60)

print("\nInterpolation Weights:")
print("Lambda 1 (Trigram) =", lambda1)
print("Lambda 2 (Bigram)  =", lambda2)
print("Lambda 3 (Unigram) =", lambda3)

print("\nIndividual Probabilities:")
print("Trigram =", round(p_is_trigram, 4))
print("Bigram  =", round(p_is_bigram, 4))
print("Unigram =", round(p_is_unigram, 4))

print("\nFormula:")
print(
    "P(is | data, science) = "
    "λ1 P(is | data, science) + "
    "λ2 P(is | science) + "
    "λ3 P(is)"
)

print("\nCalculation:")

print(
    f"= ({lambda1} × {p_is_trigram:.4f}) "
    f"+ ({lambda2} × {p_is_bigram:.4f}) "
    f"+ ({lambda3} × {p_is_unigram:.4f})"
)

print(
    f"\nInterpolated Probability = "
    f"{interpolated_probability:.4f}"
)


p_data = unigram_probability("data")

p_science_given_data = bigram_probability(
    "data",
    "science"
)

p_complete_sequence = (
    p_data
    * p_science_given_data
    * interpolated_probability
)


print("\n" + "=" * 60)
print("PROBABILITY OF COMPLETE SEQUENCE")
print("=" * 60)

print("\nSequence: data science is")

print(f"P(data) = {p_data:.4f}")

print(
    f"P(science | data) = "
    f"{p_science_given_data:.4f}"
)

print(
    f"P(is | data, science) = "
    f"{interpolated_probability:.4f}"
)

print("\nFormula:")

print(
    "P(data science is) = "
    "P(data) × P(science | data) "
    "× P(is | data, science)"
)

print(
    f"\nP(data science is) = "
    f"{p_data:.4f} × "
    f"{p_science_given_data:.4f} × "
    f"{interpolated_probability:.4f}"
)

print(
    f"\nComplete Sequence Probability = "
    f"{p_complete_sequence:.4f}"
)



p_is = 0.66
p_drives = 0.33


def entropy(probabilities):
    """
    Calculate Shannon Entropy:
        H(X) = -sum(P(x) * log2(P(x)))
    """

    h = 0

    for p in probabilities:

        if p > 0:
            h -= p * math.log2(p)

    return h


entropy_value = entropy([
    p_is,
    p_drives
])


print("\n" + "=" * 60)
print("4. ENTROPY ANALYSIS")
print("=" * 60)

print("\nPrediction Probabilities:")
print("P(is)     =", p_is)
print("P(drives) =", p_drives)

print("\nEntropy Formula:")
print("H(X) = -Σ P(x) log2(P(x))")

print("\nCalculation:")

print(
    f"H(X) = -[{p_is} × log2({p_is}) "
    f"+ {p_drives} × log2({p_drives})]"
)

print(f"\nEntropy = {entropy_value:.4f} bits")


print("\n" + "=" * 60)
print("FINAL RESULTS")
print("=" * 60)

print(
    f"\n1. P(science | data) = "
    f"{p_science_given_data:.4f}"
)

print(
    f"2. P(improves | data, science) "
    f"using backoff = {backoff_prob:.4f}"
)

print(
    f"3. P(is | data, science) "
    f"using interpolation = "
    f"{interpolated_probability:.4f}"
)

print(
    f"4. P(data science is) = "
    f"{p_complete_sequence:.4f}"
)

print(
    f"5. Entropy = "
    f"{entropy_value:.4f} bits"
)

print("\n" + "=" * 60)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 60)
