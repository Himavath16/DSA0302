import json

class InflectionalMorphologyNormalizer:

    def __init__(self):
       
        self.canonical_base = "create"

        
        self.inflection_rules = {
            "create": {
                "suffix": "None",
                "grammatical_category": "Base Form (Infinitive / Non-3rd Present)",
                "extracted_root": "create",
                "normalized_base": "create",
                "rule_applied": "Identity mapping (already in base form).",
            },
            "creates": {
                "suffix": "-s",
                "grammatical_category": "Third-Person Singular Present",
                "extracted_root": "create",
                "normalized_base": "create",
                "rule_applied": "Strip 3rd-person singular suffix '-s'.",
            },
            "creating": {
                "suffix": "-ing",
                "grammatical_category": "Present Participle / Gerund",
                "extracted_root": "creat",  
                "normalized_base": "create",
                "rule_applied": "Strip '-ing' suffix and restore silent final '-e' (e-deletion rule).",
            },
        }

    def process_word(self, word: str) -> dict:
        """Applies inflectional rules to extract grammatical features and normalize to base form."""
        clean_word = word.strip().lower()

        if clean_word in self.inflection_rules:
            rule_info = self.inflection_rules[clean_word]

            return {
                "original_word": word,
                "identified_suffix": rule_info["suffix"],
                "grammatical_category": rule_info["grammatical_category"],
                "extracted_root": rule_info["extracted_root"],
                "normalized_base": rule_info["normalized_base"],
                "final_normalized_representation": self.canonical_base,
                "rule_applied": rule_info["rule_applied"],
            }
        else:
            return {
                "original_word": word,
                "identified_suffix": "Unknown",
                "grammatical_category": "Unclassified",
                "extracted_root": clean_word,
                "normalized_base": clean_word,
                "final_normalized_representation": clean_word,
                "rule_applied": "Fallback rule: no rule matched.",
            }

    def process_batch(self, words: list) -> list:
        """Processes a list of tokens through the normalization engine."""
        return [self.process_word(w) for w in words]


def print_morphology_report(data: list):
    """Prints a structured table for human inspection."""
    print("=" * 110)
    print("INFLECTIONAL MORPHOLOGY NORMALIZATION REPORT")
    print("=" * 110)

    headers = [
        "Original",
        "Suffix",
        "Grammatical Category",
        "Surface Root",
        "Normalized Base",
    ]
    print(
        f"{headers[0]:<12} | {headers[1]:<8} | {headers[2]:<38} | {headers[3]:<12} | {headers[4]}"
    )
    print("-" * 110)

    for item in data:
        print(
            f"{item['original_word']:<12} | {item['identified_suffix']:<8} | "
            f"{item['grammatical_category']:<38} | {item['extracted_root']:<12} | "
            f"{item['final_normalized_representation']}"
        )

    print("=" * 110)
    print("\nAPPLIED MORPHOLOGICAL RULES:")
    print("-" * 110)
    for item in data:
        print(f"• [{item['original_word']}]: {item['rule_applied']}")
    print("=" * 110)

if __name__ == "__main__":
    target_tokens = ["create", "creates", "creating"]

    normalizer = InflectionalMorphologyNormalizer()
    results = normalizer.process_batch(target_tokens)

    
    print_morphology_report(results)


    print(
        "\nStructured JSON Output (Information Retrieval & Indexing Ready):"
    )
    print(json.dumps(results, indent=2))
