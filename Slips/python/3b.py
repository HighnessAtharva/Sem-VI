# Write a Python program to check if a given key already exists in a dictionary. If key exists replace with another key/value pair.

from collections import OrderedDict


def check_and_replace_key():
    my_dict = OrderedDict()
    my_dict["Sunday"] = "Fun Day"
    my_dict["Monday"] = "Work Day"
    my_dict["Tuesday"] = "Taco Day"
    my_dict["Wednesday"] = "Hump Day"
    my_dict["Thursday"] = "Thirsty Day"
    my_dict["Friday"] = "New Music Yay!"
    my_dict["Saturday"] = "Weekend Baby!"

    key = input("Enter a key to check: ")
    if key in my_dict:
        print("Key Found. Replace with new key/value pair.")
        new_key = input("Enter new key: ")
        new_value = input("Enter new value: ")

        # preserve order and replace key with new key/value pair
        my_dict = OrderedDict((new_key, new_value) if k ==
                              key else (k, v) for k, v in my_dict.items())

        for k, v in my_dict.items():
            print(k, v)

    else:
        print("Key not found")


check_and_replace_key()