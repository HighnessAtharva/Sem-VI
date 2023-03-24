# Write a  Python program that encrypts a message by adding a key value to every character.  	

def encypt_func(txt, shift):  
    result = str()  
    for char in txt:  
        if char.isupper():  
            result += chr((ord(char) + shift - 64) % 26 + 65)
        else:  
            result += chr((ord(char) + shift - 96) % 26 + 97)  
    return result  

txt = input('Enter a string : ')
shift = int(input('Enter a shift pattern number: '))
print(f"Encrypted Message: {encypt_func(txt, shift)}")