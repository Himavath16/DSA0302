import re
email = input("Enter Email: ")
password = input("Enter Password: ")
mobile = input("Enter Mobile Number: ")
email_pattern = r'^[A-Za-z][A-Za-z0-9._]*@[A-Za-z]+\.(com|org|edu|net|in)$'

if re.fullmatch(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!]).{8,}$'

if re.fullmatch(password_pattern, password):
    print("Strong Password")
else:
    print("Weak Password")
mobile_pattern = r'^[6-9][0-9]{9}$'

if re.fullmatch(mobile_pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
