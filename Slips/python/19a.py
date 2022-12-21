# Write a Python script using class to reverse a string word by word

class ReverseString:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        return ' '.join(self.string.split()[::-1])
    
string = input("Enter string: ")
if len(string.split()) <= 1:
    print("Oops! Need more than one word to reverse the string")
    exit(0)
    
reverse_string = ReverseString(string)
print(reverse_string.reverse())