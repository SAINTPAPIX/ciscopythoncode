# GUESSING GAME
print("WELCOME TO THE GUESSING GAME CORRECT ME IF I AM WRONG")
user_name = str(input("ENTER YOUR NAME"))
print("WELCOME", user_name)
# PICKING A NUMBER
print("""WE HAVE SELECTED A RANDOM NUMBER FROM 1 - 100 !!", "TRY TO GUESS THE NUMBER CORRECTLY!",
      "YOU WILL ALSO BE GIVEN HINT WHETHER YOUR GUESSES ARE HIGH OR LOW!
        UNTIL YOU GET THE ANSWER CORRECTLY""")
# PICK A RANDOM GUESS TO WIN
# for number in range(100):
   # print(number)

user_guess = list()
for x in range(1-100):
    guess = (input("ENTER CHOSEN NUMBER"))
    user_guess.append(guesses)
print("guess")
# FROM THE CHOSEN NUMBER
if user_guess == "53":
    print("CORRECT ANSWER")
elif user_guess < 53:
    print("TOO HIGH")
elif user_guess > 53:
    print("TOO LOW")




