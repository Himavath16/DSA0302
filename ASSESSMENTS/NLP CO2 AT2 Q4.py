import json

class MorphologicalParserNormalizer:

    def __init__(self):

        self.canonical_base = "activate"

        self.rules = {
            "activate": {
                "prefix": "None",
                "root": "act",
                "suffix": "-ivate",
                "word_class": "Verb",
                "derivational_sequence": [
                    "act (Noun/Verb)",
                    "act + -ivate -> activate (Verb: To make active)",
                ],
                "semantic_impact": "Base verb form indicating the initiation of a state or function.",
                "normalized_base": "activate",
            },
            "activation": {
                "prefix": "None",
                "root": "act",
                "suffix": "-ivate, -ion",
                "word_class": "Noun",
                "derivational_sequence": [
                    "act (Noun/Verb)",
                    "act + -ivate -> activate (Verb)",
                    "activate + -ion -> activation (Noun: The process/state of being active)",
                ],
                "semantic_impact": "Nominalization (Verb -> Noun); converts an action into a state, process, or event.",
                "normalized_base": "activate",
            },
            "reactivation": {
                "prefix": "re-",
                "root": "act",
                "suffix": "-ivate, -ion",
                "word_class": "Noun",
                "derivational_sequence": [
                    "act (Noun/Verb)",
                    "act + -ivate -> activate (Verb)",
                    "activate + -ion -> activation (Noun)",
                    "re- + activation -> reactivation (Noun: Restoring to an active state)",
                ],
                "semantic_impact": "Iterative prefixation (re-) + nominalization; denotes restoring or repeating a previously active state.",
                "normalized_base": "activate",
            },
        }

    def parse_word(self, word: str) -> dict:
        """Decomposes an input word and traces its derivational trajectory."""
        clean_word = word.strip().lower()

        if clean_word in self.rules:
            info = self.rules[clean_word]

            
            p_str = f"{info['prefix']}-" if info["prefix"] != "None" else ""
            parsed_representation = (
                f"{p_str}[{info['root']}]{info['suffix']}"
            )

            return {
                "original_word": word,
                "prefix": info["prefix"],
                "root_word": info["root"],
                "suffix": info["suffix"],
                "word_class": info["word_class"],
                "derivational_sequence": info["derivational_sequence"],
                "semantic_impact": info["semantic_impact"],
                "normalized_base": info["normalized_base"],
                "parsed_representation": parsed_representation,
            }
        else:
            return {
                "original_word": word,
                "prefix": "None",
                "root_word": clean_word,
                "suffix": "None",
                "word_class": "Unknown",
                "derivational_sequence": [f"{clean_word} (Unclassified)"],
                "semantic_impact": "N/A",
                "normalized_base": clean_word,
                "parsed_representation": f"[{clean_word}]",
            }

    def process_batch(self, words: list) -> list:
        """Processes a collection of tokens for indexing pipelines."""
        return [self.parse_word(w) for w in words]


def print_morphology_report(data: list):
    """Outputs a clean, human-readable analysis report."""
    print("=" * 110)
    print("MORPHOLOGICAL PARSING & SEMANTIC INDEXING REPORT")
    print("=" * 110)

    headers = [
        "Original",
        "Prefix",
        "Root",
        "Suffix",
        "Class",
        "Parsed Form",
        "Normalized Base",
    ]
    print(
        f"{headers[0]:<14} | {headers[1]:<8} | {headers[2]:<6} | {headers[3]:<14} | {headers[4]:<8} | {headers[5]:<22} | {headers[6]}"
    )
    print("-" * 110)

    for item in data:
        print(
            f"{item['original_word']:<14} | {item['prefix']:<8} | {item['root_word']:<6} | "
            f"{item['suffix']:<14} | {item['word_class']:<8} | {item['parsed_representation']:<22} | {item['normalized_base']}"
        )

    print("=" * 110)
    print("\nDERIVATIONAL SEQUENCES & SEMANTIC IMPACT:")
    print("-" * 110)
    for item in data:
        chain = " ➔ ".join(item["derivational_sequence"])
        print(f"• [{item['original_word']}]")
        print(f"  - Derivation Chain : {chain}")
        print(f"  - Semantic Shift   : {item['semantic_impact']}\n")
    print("=" * 110)

if __name__ == "__main__":
    target_tokens = ["activate", "activation", "reactivation"]

    parser = MorphologicalParserNormalizer()
    results = parser.process_batch(target_tokens)

   
    print_morphology_report(results)

    print(
        "\nStructured JSON Output (Document Classification & Indexing Pipeline Ready):"
    )
    print(json.dumps(results, indent=2))
