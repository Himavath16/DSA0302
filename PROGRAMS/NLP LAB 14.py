def check_agreement(subject, verb):
    singular = ["he", "she", "it"]
    plural = ["they", "we", "you"]

    if subject.lower() in singular and verb.lower() == "runs":
        return True

    if subject.lower() in plural and verb.lower() == "run":
        return True

    return False


subject = input("Enter subject: ")
verb = input("Enter verb: ")

if check_agreement(subject, verb):
    print("Agreement is correct")
else:
    print("Agreement is incorrect")
