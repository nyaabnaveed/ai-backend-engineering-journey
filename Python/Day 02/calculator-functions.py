'''
Task 1 — Calculator Functions

Khud se ek program banao jisme 4 functions hon:

add(a,b)
subtract(a,b)
multiply(a,b)
divide(a,b)

Phir user se 2 numbers lo aur operation select karwao.
'''

def add(a,b):
    c = a + b
    return c

def subtract(a,b):
    c = a - b
    return c

def multiply(a,b):
    c = a * b
    return c

def divide(a,b):
    c = a / b
    return c

def remainder(a,b):
    c = a % b
    return c

def exponent(a,b):
    c = a ** b
    return c

print("Welcome to the Calculator Program!")

choice = 'yes'
while (choice == 'yes'):
    a = float(input("\nEnter a number: "))
    b = float(input("Enter another number: "))

    print("\n--- CALCULATION OPTIONS ---\n1.\tAddition\n2.\tSubtraction\n3.\tMultiplication\n4.\tDivision\n5.\tRemainder\n6.\tExponentiation\n")
    num = int(input("Enter your choice: "))
    if num == 1:
        result = add(a,b)
        print(a, ' + ', b, ' = ', result)
    elif num == 2:
        result = subtract(a,b)
        print(a, ' - ', b, ' = ', result)
    elif num == 3:
        result = multiply(a,b)
        print(a, ' * ', b, ' = ', result)
    elif num == 4:
        result = divide(a,b)
        print(a, ' / ', b, ' = ', result)
    elif num == 5:
        result = remainder(a,b)
        print(a, ' % ', b, ' = ', result)
    elif num == 6:
        result = exponent(a,b)
        print(a, ' ^ ', b, ' = ', result)
    else:
        print("Invalid Choice!")
        continue

    choice = input("Do you want to continue? (yes/no): ")

print("\nExiting...\n\nThankyou!!")