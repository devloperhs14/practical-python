# randon no -> assing
# user input -> guess no 
# guess > random no -> greater than guess, please try again
# guess < random no -> less than guess, please try again
# guess = random no -> won!
# count -> tries -> result

# guess
import random
guess = random.randint(1,100) # guess
print(guess)

#vars
counter = 0
user_guess = None

#greet
print("Welcome to number guessing game.")
print("I have thought of a number between 1, 100, can you guess it?")

while user_guess != guess:
    user_guess = int(input("Enter your guessed no: "))

    counter+=1 #counter = counter+1

    # logic
    if (user_guess < guess):
        print("less than orignal guess, please try again")
    elif (user_guess>guess):
        print("greater than guess, please try again")
    else:
        print(f'Your won the game in {counter} attempts')
