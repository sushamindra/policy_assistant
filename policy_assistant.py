policies = [
    {
        "text": "Interns in India receive 5 paid leave days during their internship.",
        "employee_group": "intern",
        "country": "India",
        "source": "Leave Policy - India, Interns"
    },
    {
        "text": "Full-time employees in India receive 20 paid leave days per year.",
        "employee_group": "full_time",
        "country": "India",
        "source": "Leave Policy - India, Full-Time Employees"
    },
    {
        "text": "Interns in the United States receive 3 paid leave days during their internship.",
        "employee_group": "intern",
        "country": "United States",
        "source": "Leave Policy - United States, Interns"
    },
    {
        "text": "Interns in India may take 2 paid sick leave days during their internship.",
        "employee_group": "intern",
        "country": "India",
        "source": "Leave Policy - India, Intern Sick Leave"
    },
]


def retrieve_policy(question, employee_group, country):
    question_words = set(
        question.lower()
        .replace("?", "")
        .replace(".", "")
        .split()
    )

    common_words = {
        "how", "many", "do", "i", "get", "what", "is",
        "the", "a", "in", "for", "my", "are"
    }
    question_words -= common_words

    best_policy = None
    best_score = 0

    for policy in policies:
        if (
            policy["employee_group"] != employee_group
            or policy["country"].lower() != country.lower()
        ):
            continue

        policy_words = set(
            policy["text"].lower()
            .replace(",", "")
            .replace(".", "")
            .split()
        )

        score = len(question_words & policy_words)

        if score > best_score:
            best_policy = policy
            best_score = score

    return best_policy

    
def build_prompt(question, policy):
    prompt = f"""
    Answer the employee using only the policy passage below.
    If the passage does not contain the answer, say that the policy does not specify it.
    Do not add facts that are missing from the passage.

    Policy passage:
    {policy["text"]}

    Source:
    {policy["source"]}

    Employee question:
    {question}

    Answer:
    """
    
    return prompt


question = input("What would you like to know about the policy? ")
employee_group = input("Employee group (intern or full_time): ")
country = input("Country (India or United States): ")

employee_group = employee_group.strip().lower().replace("-", "_")
country = country.strip()

result = retrieve_policy(question,employee_group, country)

if result:
    prompt = build_prompt(question, result)
    print("\nPrompt prepared for the LLM:")
    print(prompt)
else:
    print("\nI couldn't find a matching policy.")