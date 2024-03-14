number = 10
guessed = False
guess = 'a'
limit = 3

while guess != "q" and guessed != True and limit != 0 :
    print("I'm thinking of a number...")
    guess = input("What number am I thinking of? ")
    if guess == "q":
        print(f"Sorry! The number was {number}.")
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        guessed = True
    else:
        limit -= 1
        if limit == 0:
            print(f"Sorry! The number was {number}.")
        else:
            print(f"Sorry! Try Again! You have ", limit, " guesses left. Press q to quit")
    
