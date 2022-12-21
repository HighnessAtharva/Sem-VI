# Write a Python program to check if a given key already exists in a dictionary. If key exists replace with another key/value pair.   

days = {
    "Sunday": "Fun Day",
    "Monday": "Work Day",
    "Tuesday": "Taco Day",
    "Wednesday": "Hump Day",
    "Thursday": "Thirsty Day",
    "Friday": "New Music Yay!",
    "Saturday": "Weekend Baby!"
}

def check_and_replace_key():
    key = input("Enter a key to check: ")
    if key in days:
        print("Key Found. Replace with new key/value pair.")
        days[key] = "Imaginary Bulls**t"
        days["Imaginary Day"] = days.pop(key)
        print(days)
        
    else:
        print("Key not found")

check_and_replace_key()