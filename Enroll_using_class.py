import json


class enrollment:
    def __init__(self):
        # Creates a form
        self.form_name = input("Enter the form name:  \n\t")
        question = self.question_type()
        self.save_form()

    def question_type(self):
        self.Questions = []
        while True:
            self.Question = self.question_types()
            self.Questions.append(self.Question)
            exit_ = input("Do you want to add another question (y/n)")
            if exit_ == "n":
                break

    def question_types(self):
        self.Question_type = ("number", "text", "email", "choice")
        self.que = input("Enter the question")
        while True:
            self.que_type = input(f"Enter the type{self.Question_type}")

            if self.que_type in self.Question_type:
                break
            print("Please select valid Option")

        self.question = {"query": self.que, "type": self.que_type}
        return self.question

    def save_form(self):
        # Saves the form in json.
        with open(str(self.form_name) + ".json", "w") as f:
            json.dump(self.Questions, f, indent=2)


person1 = enrollment()
