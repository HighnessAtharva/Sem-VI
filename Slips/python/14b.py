# Write a python program to fully reverse the contents of file and write it in another file.

with open("14B-file1.txt", "r") as f:
    data = f.read()[::-1]
    with open("14B-file2.txt", "w") as f2:
        f2.write(data)

print("Success. Check 14B-file2.txt and get a taste of the Upside Down. 😉")
