import re

resumes = [
    "John Doe\njohn.doe@email.com\n9876543210\n5 years of experience\nSkills: Python, SQL, Machine Learning",
    "Jane Smith\njane.smith@work.org\n8765432109\n1 year of experience\nSkills: Java, SQL",
    "Alice Johnson\nalice.j@web.com\n+91 9998887776\n3 years exp\nSkills: NLP, Python"
]

def parse_and_filter(resume_list):
    skills_list = ['Python', 'Java', 'SQL', 'Machine Learning', 'NLP']
…       
        print(f"Candidate: {name} | Email: {email} | Exp: {exp} years | Skills: {', '.join(skills)}")

        if exp >= 2 and 'Python' in skills:
            print(f"   [ELIGIBLE & SHORTLISTED]\n")
        else:
            print(f"   [NOT ELIGIBLE]\n")

parse_and_filter(resumes)




import re

def validate_portal_registration(student_profile):

    validation_rules = {
        "Register Number": r"^\d{4}[A-Z]{2}\d{3}$",     
        "Institutional Email": r"^[\w.-]+@university\.edu$", 
        "Course Code": r"^[A-Z]{2,4}\d{3}$",              
        "Semester": r"^[1-8]$",                           
        "Mobil…in(failed_validations)}")
    print("=" * 50 + "\n")

student_a = {"Name": "Alex", "Register Number": "2024CS089", "Institutional Email": "a@university.edu", "Course Code": "CSE302", "Semester": "5", "Mobile Number": "9876543210"}
student_b = {"Name": "Sarah", "Register Number": "24CS08", "Institutional Email": "s@gmail.com", "Course Code": "cs302", "Semester": "9", "Mobile Number": "12345"}

validate_portal_registration(student_a)
validate_portal_registration(student_b)







import re
product_catalog = [
    "Apple iPhone 15 Pro",
    "Apple MacBook Pro M3",
    "Samsung Galaxy S24 Ultra",
    "Samsung Galaxy Buds2 Pro",
    "Sony WH-1000XM5 Wireless Headphones",
    "Sony PlayStation 5",
…search_products("Pro", search_type="suffix")
    
def search_products(query, search_type="partial"):
    """
    Searches the product catalog using regular expressions based on the search type.
    Options: 'exact', 'prefix', 'suffix', 'partial'
…    regex_compiled = re.compile(pattern, re.IGNORECASE)

    # Filter catalog
    for product in product_catalog:
        if regex_compiled.search(product):
            matched_products.append(product)

    # Generate and display report
    print(f"--- Search Report [{search_type.upper()} MATCH] ---")
    print(f"Query Term      : '{query}'")
…search_products("Pro", search_type="suffix")

search_products("less", search_type="partial")
search_products("hp spectre x360", search_type="exact")
search_products("Apple", search_type="prefix")
search_products("Pro", search_type="suffix")


search_products("less", search_type="partial")
