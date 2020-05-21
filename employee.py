class Employee:
    raise_pct = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

    def apply_raise(self):
        self.pay = self.pay * self.raise_pct
