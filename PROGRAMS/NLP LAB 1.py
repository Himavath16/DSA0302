import re

text = "My email is student123@gmail.com and my phone number is 9876543210."
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
email = re.search(email_pattern, text)

if email:
    print("Email found:", email.group())
else:
    print("Email not found.")
phone_pattern = r'\b\d{10}\b'
phone = re.search(phone_pattern, text)

if phone:
    print("Phone number found:", phone.group())
else:
    print("Phone number not found.")
words = re.findall(r'\bs\w*', text, re.IGNORECASE)
print("Words starting with 's':", words)
