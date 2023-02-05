# Write a python script to define the class Person having members name, address. Create a subclass called Employee with member salary. Create 'n' objects of the Employee class and display all the details of the employees.

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")


class Employee(Person):
    def __init__(self, name, address, salary):
        super().__init__(name, address)
        self.salary = salary

    def display(self):
        super().display()
        print(f"Salary: {self.salary}")


n = int(input("Enter total employees: "))
employees = [Employee(input("Enter name: "), input(
    "Enter address: "), int(input("Enter salary: "))) for _ in range(n)]
for employee in employees:
    employee.display()
    print("=================================")
