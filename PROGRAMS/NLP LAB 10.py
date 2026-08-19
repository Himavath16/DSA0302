
tags = {
    "The": "NN",
    "cat": "NN",
    "runs": "NN"
}


if tags["The"] == "NN":
    tags["The"] = "DT"

if tags["runs"] == "NN":
    tags["runs"] = "VB"

for word, tag in tags.items():
    print(word, "->", tag)
