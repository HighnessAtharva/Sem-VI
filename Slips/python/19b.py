# Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.

class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

    def display(self):
        print(f"Student name: {self.student_name}")
        print(f"Marks: {self.marks}")


student1 = Student("Light Yagami", 99)
student2 = Student("L", 97)
print("Original values", end="\n===============\n")
student1.display()
student2.display()

student1.student_name = "Ryuk"
student1.marks = 100
student2.student_name = "Misa Amane"
student2.marks = 98

print("\n===============")
print("Modified values")
student1.display()
student2.display()
