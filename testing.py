# Grading system
student_name = str(input("ENTER NAME"))
student_matno = int(input("ENTER MATRIC SERIAL NUMBER"))
if student_matno <= 4:
    print("INVALID SERIAL NUMBER")
student_department = str(input('ENTER DEPARTMENT'))
student_score = int(input("SCORE"))
if student_score >= 80:
    print('A')
elif student_score <= 79:
    print("B")
elif student_score <= 60:
    print("C")
elif student_score <= 59:
    print("D")
elif student_score <= 40:
    print("F")

