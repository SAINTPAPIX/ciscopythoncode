# simple interest calculator
import math

print("hi, welcome to my simple interest calculator")
user_name = str(input("what is your name? "))
prin = float(input("enter val. of principal "))
rate = float(input("enter val. of rate "))
times = float(input("for how many years? "))
simp_interest = (prin * rate * times)/100

print("HI", user_name, " you simple interest for ",prin, "is = ", simp_interest)

# volume of a cylinder
print("THIS IS THE VOLUME OF A CYLINDER")
pi = float(input("3.142"))
radius = float(input("enter radius"))
height = float(input("enter height"))
volume_of_a_cylinder = (pi * (radius ** 2) * height)
print("the volume of your cylinder is", volume_of_a_cylinder)