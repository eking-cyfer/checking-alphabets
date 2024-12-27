# Program to check if the given character is an alphabet

# Input from user
char = input("Enter a character: ")

# Check if the character is an alphabet
if char.isalpha():
    print(f"'{char}' is an alphabet.")
else:
    print(f"'{char}' is not an alphabet.")
