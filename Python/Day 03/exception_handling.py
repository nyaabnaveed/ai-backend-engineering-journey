'''
Ek division program banao jo:

normal division kare
0 se divide karne par crash na ho
text input dene par crash na ho
'''

print("\n----- EXCEPTION HANDLING PROGRAM -----\n")

try:
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    result = float(num1)/float(num2)
    print(f"{num1} / {num2} = {result}")
except ZeroDivisionError:
    print("Can not divide by zero!")
except ValueError:
    print("Invalid Input!")

print("Exiting the program...")