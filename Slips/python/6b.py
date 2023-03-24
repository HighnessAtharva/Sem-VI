# Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String prints the string in upper case.
# Further modify the program to reverse a string word by word and print it in lower case.

class StringOperations:
    def get_string(self):
        self.s = input("Enter a string: ")

    def print_string(self):
        print(self.s.upper())

    def reverse_string(self):
        print(" ".join(self.s.lower().split()[::-1]))


my_string = StringOperations()
my_string.get_string()
my_string.print_string()
my_string.reverse_string()
