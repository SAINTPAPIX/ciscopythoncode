print("MALARIA BOT")
yes_count = 0
total_questions = 7
user_name = input("what is your name?")
print("WELCOME TO YOUR MALARIA TEST" ,  user_name)
for x in "LETS GET STARTED THEN" :
    print(x)
print("JUST A REMINDER, ALWAYS REMEMBER THAT WITH A PEACEFUL MIND, LIFE IS EASIER ")
print(" please read the following questions thoroughly and answer accurately")
# 1st test
question_1 = input("have you experienced fever? ")
if question_1 == "yes":
    yes_count+= 1
    print("A SIGN OF MALARIA DETECTED")
elif question_1 == "no":
    print("NO SIGN DETECTED")
question_2 = input("have you experienced fatigue?")

if question_2 == "yes":
    yes_count += 1
    print("A SIGN OF MALARIA DETECTED")
elif question_2 == "no":
    print("NO SIGN DETECTED")
question_3 = input("have you experienced malaise?")

if question_3 == "yes":
    yes_count += 1
    print("A SIGN OF MALARIA DETECTED")
elif question_3 == "no":
    print("NO SIGN DETECTED")
question_4 = input("have you experienced shivering?")

if question_4 == "yes":
    yes_count += 1
    print("A SIGN OF MALARIA DETECTED")
elif question_4 == "no":
    print("NO SIGN DETECTED")
question_5 = input("have you experienced severe sweating?")

if question_5 == "yes":
    yes_count += 1
    print("A SIGN OF MALARIA DETECTED")
elif question_5 == "no":
    print("NO SIGN DETECTED")
question_6 = input("have you experienced nausea?")

if question_6 == "yes":
    yes_count += 1
    print("A SIGN OF MALARIA DETECTED")
elif question_6 == "no":
    print("NO SIGN DETECTED")
question_7 = input("have you experienced vomiting?")

if question_7 == "yes":
    yes_count += 1
    print("A SIGN OF MALARIA DETECTED")
elif question_7 == "no":
    print("NO SIGN DETECTED")
malaria_probability =(yes_count//total_questions)*100
print("THE POSSIBILITY OF YOU HAVING MALARIA IS" , malaria_probability)





