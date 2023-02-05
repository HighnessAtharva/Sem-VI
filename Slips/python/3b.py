# Write a Python program to check if a given key already exists in a dictionary. If key exists replace with another key/value pair.
from collections import OrderedDict
days = {
    "Sunday": "Fun Day",
    "Monday": "Work Day",
    "Tuesday": "Taco Day",
    "Wednesday": "Hump Day",
    "Thursday": "Thirsty Day",
    "Friday": "New Music Yay!",
    "Saturday": "Weekend Baby!"
}


def check_and_replace_key(days=dict()):
    key = input("Enter a key to check: ")
    if key in days:
        print("Key Found. Replace with new key/value pair.")
        new_key = input("Enter new key: ")
        new_value = input("Enter new value: ")

        # preserve order and replace key with new key/value pair
        days = OrderedDict((new_key, new_value) if k ==
                           key else (k, v) for k, v in days.items())

        for k, v in days.items():
            print(k, v)

    else:
        print("Key not found")


check_and_replace_key(days)
