import json
class MorphologicalParser:

    def __init__(self):
 
        self.rules = {
            "disagree": {
                "prefix": "dis-",
                "root": "agree",
                "suffix": "None",
                "category": "Derivational (Prefixation)",
                "semantic_impact": "Negates the positive core meaning; shifts polarity from positive to negative.",
                "normalized_base": "agree",
                "sentiment_polarity": "Negative",
            },
            "agreement": {
                "prefix": "None",
                "root": "agree",
                "suffix": "-ment",
                "category": "Derivational (Nominalization)",
                "semantic_impact": "Transforms an action (Verb) into a state or result of harmony (Noun); retains positive polarity.",
                "normalized_base": "agree",
                "sentiment_polarity": "Positive",
            },
            "agreeable": {
                "prefix": "None",
                "root": "agree",
                "suffix": "-able",
                "category": "Derivational (Adjectivization)",
                "semantic_impact": "Converts an action (Verb) into a disposition/trait (Adjective); retains positive polarity.",
                "normalized_base": "agree",
                "sentiment_polarity": "Positive",
            },
        }

    def parse_word(self, word: str) -> dict:
        """Parses a target word using rule-based morphological decomposition."""
        clean_word = word.strip().lower()

        if clean_word in self.rules:
            info = self.rules[clean_word]
            return {
                "original_word": word,
                "prefix": info["prefix"],
                "root": info["root"],
                "suffix": info["suffix"],
                "transformation_category": info["category"],
                "semantic_interpretation": info["semantic_impact"],
                "normalized_base": info["normalized_base"],
                "sentiment_polarity": info["sentiment_polarity"],
            }
        else:
            return {
                "original_word": word,
                "prefix": "Unknown",
                "root": clean_word,
                "suffix": "Unknown",
                "transformation_category": "Unclassified",
                "semantic_interpretation": "N/A",
                "normalized_base": clean_word,
                "sentiment_polarity": "Neutral",
            }

    def process_batch(self, words: list) -> list:
        """Processes a list of words through the morphological parser."""
        return [self.parse_word(w) for w in words]


def print_structured_report(parsed_data: list):
    """Generates a human-readable table for morphological and sentiment analysis."""
    print("=" * 105)
    print("MORPHOLOGICAL ANALYSIS & SENTIMENT PARSING REPORT")
    print("=" * 105)

    headers = [
        "Original",
        "Prefix",
        "Root",
        "Suffix",
        "Category",
        "Polarity",
        "Normalized Base",
    ]
    print(
        f"{headers[0]:<12} | {headers[1]:<8} | {headers[2]:<8} | {headers[3]:<8} | {headers[4]:<30} | {headers[5]:<10} | {headers[6]}"
    )
    print("-" * 105)

    for item in parsed_data:
        print(
            f"{item['original_word']:<12} | {item['prefix']:<8} | {item['root']:<8} | "
            f"{item['suffix']:<8} | {item['transformation_category']:<30} | "
            f"{item['sentiment_polarity']:<10} | {item['normalized_base']}"
        )

    print("=" * 105)
    print("\nSEMANTIC IMPACT ANALYSIS:")
    print("-" * 105)
    for item in parsed_data:
        print(
            f"• [{item['original_word']}]: {item['semantic_interpretation']}"
        )
    print("=" * 105)

if __name__ == "__main__":
    target_words = ["disagree", "agreement", "agreeable"]

    parser = MorphologicalParser()
    results = parser.process_batch(target_words)

    print_structured_report(results)

    print("\nStructured Output for Sentiment Analysis Integration:")
    print(json.dumps(results, indent=2))
