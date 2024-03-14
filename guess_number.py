number = 10
guessed = False
guess = 'a'
limit = 5

while guess != "q" and guessed != True and limit != 0 :
    print("Press q to quit.") 
    print("I'm thinking of a number...")
    guess = input("What number am I thinking of? ")
    if guess == "q":
        print(f"Sorry! The number was {number}.")
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        guessed = True
    elif int(guess) != number:
        limit -= 1
        if int(guess) > number:
            print(f"Sorry! Your guess is too high.")
        elif int(guess) < number:
            print(f"Sorry! Your guess is too low.")
        print(f"You have ", limit, " guesses left.")        
        
            
    
