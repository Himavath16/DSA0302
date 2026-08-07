import json

class RuleBasedMorphologicalAnalyzer:

    def __init__(self):
    
        self.canonical_root = "analyze"

        self.morpho_rules = {
            "analyzing": {
                "root": "analyze",
                "affixes": ["-ing"],
                "affix_type": "suffix",
                "transformation_type": "Inflectional",
                "explanation": "Pertains to verb tense (Present Participle); keeps syntactic category (Verb).",
            },
            "analysis": {
                "root": "analyze",
                "affixes": ["-sis"],
                "affix_type": "suffix",
                "transformation_type": "Derivational",
                "explanation": "Changes syntactic category from Verb to Noun.",
            },
            "analytical": {
                "root": "analyze",
                "affixes": ["-tic", "-al"],
                "affix_type": "suffix",
                "transformation_type": "Derivational",
                "explanation": "Changes syntactic category from Verb to Adjective.",
            },
        }

    def analyze_word(self, word: str) -> dict:
        """Processes an input word using morphological rules and normalizes it for search indexing."""
        clean_word = word.strip().lower()

        if clean_word in self.morpho_rules:
            rule_info = self.morpho_rules[clean_word]

            return {
                "original_word": word,
                "extracted_root": rule_info["root"],
                "identified_affixes": rule_info["affixes"],
                "transformation_type": rule_info["transformation_type"],
                "normalized_output": self.canonical_root,
                "explanation": rule_info["explanation"],
            }
        else:
            # Fallback for unexpected inputs
            return {
                "original_word": word,
                "extracted_root": "Unknown",
                "identified_affixes": [],
                "transformation_type": "Unclassified",
                "normalized_output": clean_word,
                "explanation": "Word not present in rule dictionary.",
            }

    def process_batch(self, words: list) -> list:
        """Processes a list of words and returns structured morphological reports."""
        return [self.analyze_word(w) for w in words]


def display_report(results: list):
    """Prints a formatted report suitable for search engine retrieval indexing."""
    print("=" * 85)
    print("MORPHOLOGICAL ANALYSIS & INDEXING REPORT")
    print("=" * 85)

    headers = [
        "Original Word",
        "Extracted Root",
        "Affixes",
        "Type",
        "Normalized Index Entry",
    ]
    print(
        f"{headers[0]:<15} | {headers[1]:<14} | {headers[2]:<12} | {headers[3]:<12} | {headers[4]}"
    )
    print("-" * 85)

    for item in results:
        affix_str = ", ".join(item["identified_affixes"]) or "None"
        print(
            f"{item['original_word']:<15} | {item['extracted_root']:<14} | {affix_str:<12} | {item['transformation_type']:<12} | {item['normalized_output']}"
        )

    print("=" * 85)

if __name__ == "__main__":
    input_words = ["analyzing", "analysis", "analytical"]

    analyzer = RuleBasedMorphologicalAnalyzer()
    report_data = analyzer.process_batch(input_words)

    # Print human-readable report
    display_report(report_data)

    # Print JSON output for search engine indexer integration
    print("\nStructured JSON Output (Search Engine Ready):")
    print(json.dumps(report_data, indent=2))
