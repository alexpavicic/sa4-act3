number = 10
guessed = False
guess = 'a'

while guess != "q" and guessed != True:
    print("I'm thinking of a number...")
    guess = input("What number am I thinking of? ")
    if guess == "q":
        print(f"Sorry! The number was {number}.")
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        guessed = True
    elif int(guess) > number:
        print(f"Sorry! Your guess is too high, Try Again! Press q to quit")
    elif int(guess) < number:
        print(f"Sorry! Your guess is too low, Try Again! Press q to quit")
    else:
        print(f"Sorry! Try Again! Press q to quit")
    
