# Write a file handling program in python, which opens the file ‘report.txt’ and write data into it. Use the seek() and tell() functions in python while reading the data from the file. 

with open(file='12B-file.txt', mode='w') as f:
    f.write('Hello World')
    print("[Hello World written to file]")
    print(f"Cursor Position [f.tell]->{f.tell()}")
    print(f"Cursor Position reset to zero [f.seek]->{f.seek(0)}")
    
with open(file='12B-file.txt', mode='r') as f:
    print(f"Reading from file [f.read]->{f.read()}")
