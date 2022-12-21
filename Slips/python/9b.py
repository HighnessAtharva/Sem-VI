# Write a python program to count repeated characters in a string. 
# Sample string: 'thequickbrownfoxjumpsoverthelazydog' 
# Expected output: o-4, e-3, u-2, h-2, r-2, t-2       

my_str= 'thequickbrownfoxjumpsoverthelazydog'
print("Original string: ",my_str)
counter={}
for x in my_str:
    if my_str.count(x) > 1:
        count=my_str.count(x)
        counter[x]=count

print("Repeated characters: ")
for key, value in sorted(counter.items()):
    print(key, "-", value, end=", ")

 