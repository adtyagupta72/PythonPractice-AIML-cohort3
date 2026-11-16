import random                      # Python's built-in library for random numbers

secret = random.randint(1, 100)    # pick a secret number from 1 to 100 (both included)
attempts = 0                       # count how many guesses the player makes

print("I'm thinking of a number between 1 and 100. Can you guess it?")

while True:                        # keep asking until the player wins
    text = input("Your guess: ")   # input() always gives us text, e.g. "42"

    if not text.isdigit():         # stop the program crashing if someone types "abc"
        print("Please type a whole number.")
        continue                   # skip the rest and ask again

    guess = int(text)              # turn the text "42" into the number 42
    attempts = attempts + 1        # one more guess used

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break                      # leave the loop: the game is over

# import random; 
# n, g = random.randint(1, 100), 0
# while g != n: 
#     g = int(input("Guess 1-100: ")); 
#     print("Too low" if g < n else "Too high" if g > n else "Correct!")