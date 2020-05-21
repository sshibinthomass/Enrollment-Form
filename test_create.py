import unittest
import os.path
from Enroll_using_class import enrollment


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.form = enrollment("Enrollment Form")

    def text_question_types(self):

        user_input = ["Enter name:", "text"]

        expected_question = {"query": "Enter name:", "type": "text"}

        with patch("builtins.input", side_effect=user_input):
            question = self.enrollment.question_type()
            self.assertEqual(question, expected_question)

    def test_save_form(self):
        os.path.exists("Enrollment Form.json")


if __name__ == "__main__":
    unittest.main()
