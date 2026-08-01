import re

def validate_portal_registration(student_profile):
    # Enforce precise institutional matching configurations
    validation_rules = {
        "Register Number": r"^\d{4}[A-Z]{2}\d{3}$",       # Year(4) + Dept(2) + ID(3)
        "Institutional Email": r"^[\w.-]+@university\.edu$", # University domain limits
        "Course Code": r"^[A-Z]{2,4}\d{3}$",              # Dept Code + Code Number
        "Semester": r"^[1-8]$",                           # Valid academic terms
        "Mobile Number": r"^(?:\+?91[-.\s]?)?[6-9]\d{9}$"  # Standard contact limits
    }

    failed_validations = []
    print(f" Evaluation Ledger For: {student_profile.get('Name', 'Unknown')}")

    # Run loop through standard evaluation paths
    for field_name, pattern in validation_rules.items():
        field_value = str(student_profile.get(field_name, ""))
        if re.match(pattern, field_value, re.I):
            print(f"    {field_name}: VALID ('{field_value}')")
        else:
            print(f"    {field_name}: INVALID ('{field_value}')")
            failed_validations.append(field_name)

    # Process final reporting flags
    print("-" * 50)
    if not failed_validations:
        print("STATUS :  REGISTRATION SUCCESSFUL")
        print("REASON : All submitted attributes conform to system guidelines.")
    else:
        print("STATUS :  REGISTRATION FAILED")
        print(f"REASON : Invalid format schemas detected in: {', '.join(failed_validations)}")
    print("=" * 50 + "\n")

# Input Profiles Dataset
student_a = {"Name": "Alex", "Register Number": "2024CS089", "Institutional Email": "a@university.edu", "Course Code": "CSE302", "Semester": "5", "Mobile Number": "9876543210"}
student_b = {"Name": "Sarah", "Register Number": "24CS08", "Institutional Email": "s@gmail.com", "Course Code": "cs302", "Semester": "9", "Mobile Number": "12345"}

validate_portal_registration(student_a)
validate_portal_registration(student_b)
