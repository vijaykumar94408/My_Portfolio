import random

class InvalidNumberException(Exception):
    pass

random_number = random.randint(1, 100)
attempts = 5
attempts_used = 0

print("Welcome to the Guess Number Game!")
print("Guess a number from 1 to 100 and win the game.")

while attempts > 0:
    try:
        user_guessed_number = int(input("Enter your guess: "))
        
        if user_guessed_number < 1 or user_guessed_number > 100:
            raise InvalidNumberException("Please enter a number between 1 and 100.")
        
        attempts_used += 1
        
        if user_guessed_number < random_number:
            print("Higher! Try again.")
        elif user_guessed_number > random_number:
            print("Lower! Try again.")
        else:
            print("Congratulations! Your guess is correct. Attempts used:",attempts_used)
            break
        
        attempts -= 1
        
        if attempts == 0:
            print("Sorry, you're out of attempts! The number was",random_number,"Attempts used:",attempts_used)
        else:
            print("You have attempts left:",attempts)
    
    except InvalidNumberException as e:
        print(e)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
