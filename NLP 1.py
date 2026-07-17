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
