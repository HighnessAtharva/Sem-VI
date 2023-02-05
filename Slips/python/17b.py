# Write Python program that has a class Person storing name and date of birth(DOB) of a person. Subtract the DOB from today’s date to find out whether a person is eligible to vote or not.

from datetime import datetime


class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        self.age = None

    def eligible_to_vote(self):
        self.age = datetime.now().year-int(self.dob[-4:])
        if self.age < 18:
            print(f"{self.name} is not eligible to vote.")
        else:
            print(f"{self.name} is eligible to vote.")


person1 = Person("John", "21/08/2002")
person2 = Person("Kate", "01/09/2013")

person1.eligible_to_vote()
person2.eligible_to_vote()
