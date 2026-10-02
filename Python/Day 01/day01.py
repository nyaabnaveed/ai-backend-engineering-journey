# Q1 — Conditions: 
# Take age from user 
# If age >= 18 --> Adult
# else --> Minor
print("\nQ1 — Conditions: ")

age = int(input("Please enter your age: "))
if (age >= 18):
    print("You are an ADULT")
else:
    print("You are a MINOR")

# Q2 — Loops:
# Print even numbers from 1 to 20
print ("\nQ2 — Loops: ")

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Q3 — Function:
# Make a function that takes two numbers as input and returns the maximum number.
print("\nQ3 — Function: ")

def maxNum(a,b):
    if a > b:
        return a
    else:   
        return b    

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
maximum = maxNum(num1, num2)
print("The maximum number is:", maximum)

# Q4 — Lists
# numbers = [12, 5, 8, 20, 3, 15]
# Find maximum, minimum, average
print("\nQ4 — Lists: ")

numbers = [12, 5, 8, 20, 3, 15]
print("Maximum Number = ", max(numbers))
print("Minimum Number = ", min(numbers))
print("Average = ", sum(numbers)/len(numbers))

# Q5 — Dictionary
# print name and marks
print("\nQ5 — Dictionary: ")

student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}

print("Name: ", student["name"])
print("Marks: ", student["marks"])

# Q6 — Strings
# Take string from user and count num of vowels in it
print("\nQ6 — Strings: ")

sentence = input("Enter a sentence: ")
counter = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in range(0, len(sentence)):
    if sentence[i] in vowels:
        counter = counter + 1

print("Number of vowels in your sentence = ", counter)

