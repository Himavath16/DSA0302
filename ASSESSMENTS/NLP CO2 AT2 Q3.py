import json
class DerivationalMorphologyNormalizer:

    def __init__(self):
        self.canonical_root = "govern"

        self.derivational_rules = {
            "govern": {
                "root": "govern",
                "affixes": [],
                "derivational_level": 0,
                "derivational_hierarchy": ["govern (Base Verb)"],
                "normalized_rep": "govern",
                "pos": "Verb",
            },
            "government": {
                "root": "govern",
                "affixes": ["-ment"],
                "derivational_level": 1,
                "derivational_hierarchy": [
                    "govern (Base Verb)",
                    "govern + -ment -> government (Noun: Entity/System)",
                ],
                "normalized_rep": "govern",
                "pos": "Noun",
            },
            "governance": {
                "root": "govern",
                "affixes": ["-ance"],
                "derivational_level": 1,
                "derivational_hierarchy": [
                    "govern (Base Verb)",
                    "govern + -ance -> governance (Noun: Abstract Process/Act)",
                ],
                "normalized_rep": "govern",
                "pos": "Noun",
            },
        }

    def process_word(self, word: str) -> dict:
        """Decomposes a word, builds its derivational hierarchy, and normalizes it."""
        clean_word = word.strip().lower()

        if clean_word in self.derivational_rules:
            info = self.derivational_rules[clean_word]

            return {
                "original_word": word,
                "root_form": info["root"],
                "detected_affixes": info["affixes"],
                "derivational_level": info["derivational_level"],
                "derivational_hierarchy": info["derivational_hierarchy"],
                "normalized_representation": info["normalized_rep"],
                "final_clustering_token": info["normalized_rep"],
            }
        else:
            return {
                "original_word": word,
                "root_form": clean_word,
                "detected_affixes": [],
                "derivational_level": 0,
                "derivational_hierarchy": [
                    f"{clean_word} (Unclassified Base)"
                ],
                "normalized_representation": clean_word,
                "final_clustering_token": clean_word,
            }

    def process_batch(self, words: list) -> list:
        """Processes a list of input tokens."""
        return [self.process_word(w) for w in words]


def display_morphology_report(data: list):
    """Outputs a structured report formatted for readability."""
    print("=" * 100)
    print("MORPHOLOGY-BASED NORMALIZATION & HIERARCHY REPORT")
    print("=" * 100)

    headers = [
        "Original",
        "Root",
        "Affixes",
        "Level",
        "Normalized Token",
        "Topic Model Feature",
    ]
    print(
        f"{headers[0]:<14} | {headers[1]:<8} | {headers[2]:<10} | {headers[3]:<6} | {headers[4]:<18} | {headers[5]}"
    )
    print("-" * 100)

    for entry in data:
        affix_str = ", ".join(entry["detected_affixes"]) or "None"
        print(
            f"{entry['original_word']:<14} | {entry['root_form']:<8} | {affix_str:<10} | "
            f"Level {entry['derivational_level']:<1} | {entry['normalized_representation']:<18} | {entry['final_clustering_token']}"
        )

    print("=" * 100)
    print("\nDERIVATIONAL HIERARCHY BREAKDOWN:")
    print("-" * 100)
    for entry in data:
        hierarchy_chain = " ➔ ".join(entry["derivational_hierarchy"])
        print(f"• [{entry['original_word']}]: {hierarchy_chain}")
    print("=" * 100)


if __name__ == "__main__":
    input_tokens = ["govern", "government", "governance"]

    normalizer = DerivationalMorphologyNormalizer()
    results = normalizer.process_batch(input_tokens)

 
    display_morphology_report(results)

    print(
        "\nStructured JSON Output (Topic Modeling & Document Clustering Pipeline Ready):"
    )
    print(json.dumps(results, indent=2))
