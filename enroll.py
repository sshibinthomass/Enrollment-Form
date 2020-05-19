import json


def create_form():
    """Creates a form
    """
    form_name = input("Enter the form name:  ")
    questions = request_questions()
    save_form(form_name, questions)


def request_questions():
    i = 0
    questions = []
    exit_while = "y"
    while True:
        if exit_while.lower() == "n":
            break
        else:
            question = input("Enter question {}:".format(i + 1))
            questions.append(question)
            i += 1
        exit_while = input("Do you want to add another input (y/n)? ")
    return questions


def save_form(form_name, question):
    "Saves the form in json."
    with open(str(form_name) + ".json", "w") as f:
        json.dump(question, f, indent=2)


create_form()
