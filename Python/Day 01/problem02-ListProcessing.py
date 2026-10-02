'''
Problem B — List Processing
numbers = [4, 7, 2, 9, 12, 5, 8, 3]

Program:

even numbers
odd numbers
sum
largest number
'''

print("\n--- LIST PROCESSING ---")
numbers = [4, 7, 2, 9, 12, 5, 8, 3]

# even numbers
print("Even Numbers: ")
for i in range(0,len(numbers)):
    if numbers[i] % 2 == 0:
        print(numbers[i], end=" ")

# odd numbers
print("\n\nOdd Numbers: ")
for i in range(0,len(numbers)):
    if numbers[i] % 2 != 0:
        print(numbers[i], end=" ")

# sum of numbers
print("\n\nSum of Numbers: ", sum(numbers))

# largest number
print("\nLargest Number: ", max(numbers))

