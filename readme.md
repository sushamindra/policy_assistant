# Policy Assistant

A small Python learning prototype that retrieves a fictional HR policy passage based on an employee’s question, employee group, and country. It demonstrates metadata filtering, basic keyword search, and preparing a prompt with the selected policy as evidence.

## How It Works

1. The program asks for a policy question, employee group, and country.
2. It filters the policy list using the employee group and country.
3. It compares the question’s words with each eligible policy passage.
4. It selects the passage with the most shared words.
5. It prints a prompt containing the selected passage and its source.

## Requirements

- Python 3

The program uses Python’s built-in features and does not require additional packages.

## How to Run

Open a terminal in this folder and run:

```bash
python policy_assistant.py