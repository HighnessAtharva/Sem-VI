# Write a python script to define a class student having members roll no, name, age, gender. Create a subclass called Test with member marks of 3 subjects. Create three objects of the Test class and display all the details of the student with total marks.

class Student():
    def __init__(self, roll_no, name, age, gender):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender


class Test(Student):
    def __init__(self, roll_no, name, age, gender, sub1mark, sub2mark, sub3mark):
        super().__init__(roll_no, name, age, gender)
        self.mark1 = sub1mark
        self.mark2 = sub2mark
        self.mark3 = sub3mark

    def get_all_details(self):
        self.total = self.mark1 + self.mark2 + self.mark3

        print(f"Roll no : {self.roll_no}")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")

        print(f"sub1 marks: {self.mark1}")
        print(f"sub2 marks: {self.mark2}")
        print(f"sub3 marks: {self.mark3}")
        print(f"{self.name}'s marks: {self.total}")
        print("====================================")


Test(1, "Super Saiyan Goku (SSG)", 19, 'M', 82, 89, 76).get_all_details()
Test(2, 'Frieza', 20, 'M', 94, 91, 84).get_all_details()
Test(3, 'Bulma', 17, 'F', 92, 89, 86).get_all_details()
