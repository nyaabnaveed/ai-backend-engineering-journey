'''
Task 3 — Mini Challenge

Ek function:

analyze_numbers(numbers)

jo list receive kare aur return kare:

minimum
maximum
average
even numbers
odd numbers
'''

def analyze_numbers(numbers):
    mini = min(numbers)
    maxi = max(numbers)
    average = sum(numbers)/len(numbers)
    
    Enums = []
    for i in range(0,len(numbers)):
        if numbers[i] % 2 == 0:
            Enums.append(numbers[i])
        
    Onums = []
    for i in range(0,len(numbers)):
        if numbers[i] % 2 != 0:
            Onums.append(numbers[i])
        
    result = {
        "minimum" : mini,
        "maximum" : maxi,
        "average" : average,
        "evenNumbers" : Enums,
        "oddNumbers" : Onums
    }

    return result

print("\n--- NUMBER ANALYZER ---\n")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = analyze_numbers(numbers)
print("Minimum = ", result["minimum"])
print("Maximum = ", result["maximum"])
print("Average = ", result["average"])
print("Even Numbers = ", result["evenNumbers"])
print("Odd Numbers = ", result["oddNumbers"])