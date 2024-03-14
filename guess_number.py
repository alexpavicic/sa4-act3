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
    else:
        print(f"Sorry! Try Again!, q to quit")
    
