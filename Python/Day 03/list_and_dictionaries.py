'''
Ye data use karo:

students = [
    {"name": "Ali", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "Ahmed", "marks": 67},
    {"name": "Hina", "marks": 78},
    {"name": "Usman", "marks": 25}
]

Khud functions/program banao jo:

Har student ka name + marks print kare.
Highest marks wala student find kare.
Average marks calculate kare.
Passing students ki list banaye (marks >= 35).
Failing students ki list banaye.
find_student(students, name) function banaye.
    mil jaye → student dictionary return
    na mile → None 

Bonus: Passing students ko list comprehension se bhi find karo.
'''

print("\n---------- List & Dictionary Manipulation ----------\n")

students = [
    {"name": "Ali", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "Ahmed", "marks": 67},
    {"name": "Hina", "marks": 78},
    {"name": "Usman", "marks": 25}
]

# 1. Function to print name and marks of students
def print_name_and_marks(students):
    print("\nStudent Name and Marks:")
    for i in students:
        print("Name: ", i["name"], "\tMarks: ", i["marks"])

# 2. Function to find student with highest marks
def highest_marks(students):
    highest = 0
    # finds highest marks & assigns that to highest variable
    for i in students:
        if (i["marks"] > highest):
            highest = i["marks"]

    # compares highest marks with marks of entire list and prints 
    # the name of student that has highest marks
    for i in students:
        if (i["marks"] == highest):
            print("\nStudent with highest marks: ", i["name"])

# 3. Function to print average marks
def average_marks(students):
    sum = 0
    for i in students:
        sum = sum + i["marks"]

    average = sum/len(students)
    print("\nAverage Marks: ", average)
         
# 4. Function to mke list of passing students
def passing_students(students):
    passList = []
    for i in students:
        if (i["marks"] >= 35):
            passList.append(i["name"])
    print("\nList of passing students -->", end = " ")
    for i in passList:
        print(i, end = " ")
    print()

# 5. Function to mke list of failed students
def failed_students(students):
    failList = []
    for i in students:
        if (i["marks"] < 35):
            failList.append(i["name"])
    print("\nList of failed students -->", end = " ")
    for i in failList:
        print(i, end = " ")
    print()


# 6. Function to find a student and return its details(dictionary)
def find_student(students, name):
    for i in students:
        if (i["name"] == name):
            return i
    return None

# passing students using list comprehension
def passing_students_listCmp(students):
    passList = [i["name"] for i in students if i["marks"] >= 35]
    print(passList)

# run loop and do actions according to users options until user says no
choice = "yes"
while (choice == "yes"):
    print("\nOptions:\n1.\tList of all students with their marks\n2.\tStudent with highest marks\n3.\tAverage of marks\n4.\tList of passing students\n5.\tList of failed students\n6.\tSearch student\n7.\tList of passing students (List Comprehension)")
    option = int(input("Enter your option: "))
    match option:       # alternative of switch bcz python does not have switch
        case 1:
            print_name_and_marks(students)
        case 2:
            highest_marks(students)
        case 3:
            average_marks(students)
        case 4:
            passing_students(students)
        case 5:
            failed_students(students)
        case 6:
            a = find_student(students, "Usman")
            if (a != None):
                print("Student Found!\n", a)
            else:
                print("Student not found!")
        case 7:
            print("List of passing students:")
            passing_students_listCmp(students)
        case _:
            print("Invalid Option!")

    choice = input("Do you want to continue? (yes/no): ")

print("Exiting...\n")