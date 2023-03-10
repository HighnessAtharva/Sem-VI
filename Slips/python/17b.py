# Write Python program that has a class Person storing name and date of birth(DOB) of a person. Subtract the DOB from today’s date to find out whether a person is eligible to vote or not.

from datetime import date

class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def is_eligible_to_vote(self):
        today = date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age >= 18

# Example usage:
person1 = Person("John", date(1990, 1, 1))
person2 = Person("Jane", date(2005, 6, 15))

print(person1.name, "is eligible to vote:", person1.is_eligible_to_vote())
print(person2.name, "is eligible to vote:", person2.is_eligible_to_vote())
