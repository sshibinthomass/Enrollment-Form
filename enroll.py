import json


def create_form():
    """Creates a form
    """
    form_name = input("Enter the form name:  ")
    questions = request_questions()
    save_form(form_name, questions())


def request_questions():
    questions = input("Enter your name")
    return questions


def save_form(form_name, questions):
    "Saves the form in json."
    pass

