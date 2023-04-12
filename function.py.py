# CREATING
def greeter():
    print("Good morning !.. it is a beautiful day  ye ye")
# invoking / calling
greeter()

# function that return type
def mult():
    x = 2
    z = 1
    y = 3
    return x * y * z
# invoke the function
g = mult() / 4
print(" from the function ", mult())
print(" outside compute",g)
student_names = list()
for i in range(mult()):
    names = input("ENTER STUDENT NAMES")
    student_names.append(names)
print(student_names)
# PARAMETERIZED FUNCTION
def n_AP(a,n,d):
    tn = a + (n-1)* d
    return tn
y = n_AP(2,10,3)
x = n_AP(3,4,1) * 2
print(y)
print(n_AP(2,10,3))
print(x)


