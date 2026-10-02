'''
Task 2 — Student Result Function

Function banao:

calculate_grade(marks)

Jo marks receive kare aur grade return kare.

Phir doosra function:

is_passed(marks)

Jo True ya False return kare.
'''

def calculate_grade(marks):
    if (marks >= 90):
        grade = 'A'
        return grade

    elif (marks >= 80):
        grade = 'B'
        return grade

    elif (marks >= 70):
        grade = 'C'
        return grade

    elif (marks >= 60):
        grade = 'D'
        return grade

    elif (marks >= 35):
        grade = 'E'
        return grade
    
    else:
        grade = 'F'
        return grade

def is_passed(marks):
    if (marks >= 35):
        return True
    else:
        return False

print("\n--- RESULT PORTAL ---\n")

marks = float(input("Enter your marks: "))
while (marks > 100 or marks < 0):
    print("Invalid Marks!")
    marks = float(input("Enter your marks again: "))

grade = calculate_grade(marks)
status = is_passed(marks)
print("\nRESULT\n")
if status == True:
    print("Status = Passed")
else:
    print("Status = Failed")

print("Grade = ", grade, "\n")