# Write a Python script to sort (ascending and descending order)  a dictionary by key.

radiohead_discography = {
    "The Bends": 1995,
    "OK Computer": 1997,
    "Kid A": 2000,
    "Amnesiac": 2001,
    "Hail to the Thief": 2003,
    "In Rainbows": 2007,
    "The King of Limbs": 2011,
    "A Moon Shaped Pool": 2016,
}

print("Sorted by key (ascending):")
for key in sorted(radiohead_discography):
    print(key, radiohead_discography[key])

print("=====================================")

print("Sorted by key (descending):")
for key in sorted(radiohead_discography, reverse=True):
    print(key, radiohead_discography[key])
