import random
num_to_guess = random.randint(1,100)
num_guesses = 0

while num_guesses < 5:
    player_guess = int(input("Guess a Number: "))
    if player_guess == num_to_guess:
        print("You guessed it")
        print("Game Over. You Win!!!!")
    else:
        num_guesses += 1
        if num_guesses != 5:
           print("Guess again")
           if num_to_guess - player_guess < 0:
               print("Guess Lower")
           else: 
               print("Guess Higher")
        
        

if player_guess != num_to_guess: 
    print("Game Over!")
    print("The number was: ", num_to_guess)

