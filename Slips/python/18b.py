# Define a class Employee having members id, name, department, salary. Create a subclass called Manager with member bonus. Define methods accept and display in both the classes.  Create n objects of the Manager class and display the details of the Manager having the maximum total salary (salary+bonus).

class Employee:
    def accept(self):
        self.id = int(input("Enter ID: "))
        self.name = input("Enter name: ")
        self.department = input("Enter department: ")
        self.salary = int(input("Enter salary: "))

    def display(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")


class Manager(Employee):
    def accept(self):
        super().accept()
        self.bonus = int(input("Enter bonus: "))

    def display(self):
        super().display()
        print(f"Bonus: {self.bonus}")

    def total_salary(self):
        return self.salary + self.bonus


n = int(input("Enter number of managers: "))
managers = []
max_salary = 0
for _ in range(n):
    manager = Manager()
    manager.accept()
    managers.append(manager)
    if manager.total_salary() > max_salary:
        max_salary = manager.total_salary()
        max_salary_manager = manager

print(
    f"Manager {max_salary_manager.name} has maximum total salary: {max_salary}")
