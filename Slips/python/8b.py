# Write a Python script using class, which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case     

class StringOperation:
    def __init__(self):
        self.str = ''
    def get_String(self):
        self.str = input('Enter a string: ')
    def print_String(self):
        print(self.str.upper())
        
str_obj = StringOperation()
str_obj.get_String()
str_obj.print_String()
