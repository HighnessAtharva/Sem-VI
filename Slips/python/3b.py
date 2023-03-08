# Write a Python program to check if a given key already exists in a dictionary. If key exists replace with another key/value pair.

from collections import OrderedDict


def check_and_replace_key():
    my_dict = OrderedDict({
        "Sunday": "Fun Day",
        "Monday": "Work Day",
        "Tuesday": "Taco Day",
        "Wednesday": "Hump Day",
        "Thursday": "Thirsty Day",
        "Friday": "New Music Yay!",
        "Saturday": "Weekend Baby!"

    })

    key = input("Enter a key to check: ")
    if key in my_dict:
        print("Key Found. Replace with new key/value pair.")
        new_value = input("Enter new value: ")

        my_dict[key] = new_value
        for k, v in my_dict.items():
            print(k, v)

    else:
        print("Key not found")


check_and_replace_key()
