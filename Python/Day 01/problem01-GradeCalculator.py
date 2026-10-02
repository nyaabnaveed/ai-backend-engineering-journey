'''
Problem A — Grade Calculator

Marks input:

90+    A
80–89  B
70–79  C
60–69  D
<60    F
'''

print("\n--- GRADE CALCULATOR ---")
marks = float(input("Enter your marks: "))
if (marks > 100 or marks < 0):
    print("Invalid Marks!")
else:
    if (marks < 101 and marks >= 0):
        if (marks >= 90):
            print("Your grade = A")

        elif(marks >= 80):
            print("Your grade = B")

        elif(marks >= 70):
            print("Your grade = C")

        elif(marks >= 60):
            print("Your grade = D")

        else:
            print("Your grade = F")

