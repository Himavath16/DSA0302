import re
product_catalog = [
    "Apple iPhone 15 Pro",
    "Apple MacBook Pro M3",
    "Samsung Galaxy S24 Ultra",
    "Samsung Galaxy Buds2 Pro",
    "Sony WH-1000XM5 Wireless Headphones",
    "Sony PlayStation 5",
…search_products("Pro", search_type="suffix")
search_products("less", search_type="partial")
    escaped_query = re.escape(query)

    if search_type == "exact":
        # Matches the exact string from start to finish
        pattern = rf"^{escaped_query}$"
    elif search_type == "prefix":
…search_products("Pro", search_type="suffix")
search_products("less", search_type="partial")
search_products("hp spectre x360", search_type="exact")
search_products("Apple", search_type="prefix")
if search_type == "exact":
        pattern = rf"^{escaped_query}$"
    elif search_type == "prefix":
