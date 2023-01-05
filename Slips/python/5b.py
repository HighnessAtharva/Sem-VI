# Write Python script to create two text files. Enter data in each file and merge the data in the third file.

def merge_two_files(file1, file2):  # sourcery skip: path-read
    with open(file1) as f:
        data1 = f.read()
    with open(file2) as f:
        data2 = f.read()
    with open("5B_file3.txt", "w") as f:
        f.write(data1)
        f.write("\n")
        f.write(data2)
    print("Files merged successfully. Check 5B_file3.txt")


with open("5B_file1.txt", "w") as f:
    f.write("This is file 1.")

with open("5B_file2.txt", "w") as f:
    f.write("This is file 2.")

merge_two_files("5B_file1.txt", "5B_file2.txt")