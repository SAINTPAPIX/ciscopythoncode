print("this program calculates the average of 2 students ages")
n=int(input("enter the numbers of the students"))
number_of_students = n
student_age = []
for age in range(number_of_students):
    age_collector=int(input("enter your age"))
    student_age.append(age_collector)
student_age.sort()
for x in student_age :
    print(x)
a=str(input('Sum'))
if a== "sum":
    z=sum(student_age)
    print("the sum is", z)
if  a == 'Average':
    add=sum(student_age)
    v=add/number_of_students
    print('the average is',v)
if a=='both':
    z=sum(student_age)
    v=sum(student_age)/number_of_students
    print('sum=',z, 'AND', 'Average=',v)
