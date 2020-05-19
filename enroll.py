import json


def create_form():
    """Creates a form
    """
    form_name = input("Enter the form name:  ")
    question = request_questions()
    save_form(form_name, question)


def request_questions():
    i = 0
    question = []
    while True:
        exit_while = input("Do you want to add another input (y/n)? ")
        if exit_while.lower() == "n":
            break
        else:
            question.append(input("Enter question {}:".format(i + 1)))
            i += 1
    return question


def save_form(form_name, question):
    "Saves the form in json."
    with open(str(form_name) + ".json", "w") as f:
        json.dump(question, f, indent=2)


create_form()
