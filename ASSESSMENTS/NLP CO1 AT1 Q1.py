import re
resumes = [
    "John Doe\njohn.doe@email.com\n9876543210\n5 years of experience\nSkills: Python, SQL, Machine Learning",
    "Jane Smith\njane.smith@work.org\n8765432109\n1 year of experience\nSkills: Java, SQL",
    "Alice Johnson\nalice.j@web.com\n+91 9998887776\n3 years exp\nSkills: NLP, Python"
]
def parse_and_filter(resume_list):
    skills_list = ['Python', 'Java', 'SQL', 'Machine Learning', 'NLP']

    print("--- SHORTLISTED CANDIDATES ---")
    for res in resume_list:
        name = res.strip().split('\n')[0]
        email = re.search(r'[\w.-]+@[\w.-]+\.\w+', res).group(0)
        phone = re.search(r'(?:\+?\d{1,3}[-.\s]?)?\d{10}', res).group(0)
        exp = int(re.search(r'(\d+)\s*years?', res, re.I).group(1))
        skills = [s for s in skills_list if re.search(rf'\b{s}\b', res, re.I)]
        print(f"Candidate: {name} | Email: {email} | Exp: {exp} years | Skills: {', '.join(skills)}")
        if exp >= 2 and 'Python' in skills:
            print(f"   [ELIGIBLE & SHORTLISTED]\n")
        else:
            print(f"   [NOT ELIGIBLE]\n")
parse_and_filter(resumes)
