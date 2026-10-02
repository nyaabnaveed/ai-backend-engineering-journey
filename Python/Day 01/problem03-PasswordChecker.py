'''
Problem C — Password Checker

Password check karo:
length ≥ 8
at least one digit
at least one uppercase
Then:
Strong
ya
Weak
'''

print("\n--- PASSWORD CHECKER ---")
password = input("Enter your password: ")
length = False
oneDigit = False
oneUppercase = False

if (len(password) >= 8):
    length = True

oneDigit = any(char.isdigit() for char in password)
oneUppercase = any(char.isupper() for char in password)

if (length == True and oneDigit == True and oneUppercase == True):
    print("Strong Password!")
else:
    print("Weak Password!")
    if (length == False):
        print("Length is less than 8.")
    if (oneUppercase == False):
        print("Include atleast one Uppercase Letter.")
    if (oneDigit == False):
        print("Include atleast one Digit.")



