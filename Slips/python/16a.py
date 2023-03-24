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
for k, v in sorted(radiohead_discography.items()):
    print(k, v)
    
print("=====================================")

print("Sorted by key (descending):")
for k, v in sorted(radiohead_discography.items(), reverse=True):
    print(k, v)