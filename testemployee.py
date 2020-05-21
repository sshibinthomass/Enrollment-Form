import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    def setup(self):
        
    
    
    def test_Fullname(self):
        emp1 = Employee("Amit", "Sharma", "120")
        self.assertEqual(emp1.fullname, "Amit Sharma")

        emp1.last = "Thomas"

        self.assertEqual(emp1.fullname, "Amit Thomas")

    def test_email(self):
        emp1 = Employee("Amit", "Sharma", "120")
        self.assertEqual(emp1.email, "Amit.Sharma@gmail.com")

        emp1.last = "Thomas"

        self.assertEqual(emp1.email, "Amit.Thomas@gmail.com")


if __name__ == "__main__":
    unittest.main()
