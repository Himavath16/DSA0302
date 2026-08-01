import re

product_catalog = [
    "Apple iPhone 15 Pro", "Apple MacBook Pro M3", "Samsung Galaxy S24 Ultra",
    "Samsung Galaxy Buds2 Pro", "Sony WH-1000XM5 Wireless Headphones",
    "Sony PlayStation 5", "Dell XPS 13 Laptop", "HP Spectre x360",
    "Wireless Charging Pad", "Anker Power Bank 20K"
]

def search_products(query, search_type="partial"):
    q = re.escape(query)
    patterns = {
        "exact": rf"^{q}$",
        "prefix": rf"\b{q}",
        "suffix": rf"{q}\b",
        "partial": q
    }
    
    rx = re.compile(patterns.get(search_type, q), re.IGNORECASE)
    matches = [p for p in product_catalog if rx.search(p)]

    print(f"--- [{search_type.upper()}] '{query}' -> {len(matches)} found ---")
    for prod in matches:
        print(f"  - {prod}")
    print()
    return matches

# --- Test Executions ---
search_products("hp spectre x360", "exact")
search_products("Apple", "prefix")
search_products("Pro", "suffix")
search_products("less", "partial")
