def text_question(question, validator=False):
    user_input = input("Question")
    if is_valid(user_input, qtype):
        return user_input
    else:
        text_question(question,)


def is_valid():
    pass


def main():
    question = get_questions()
    for question in questions:
        test_question(question.text, question.type)
