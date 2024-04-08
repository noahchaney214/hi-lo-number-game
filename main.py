from random import randint

""" Hi-Lo Number Guessing Game

    The player will guess a randomly selected secret number. The player will be told
    if their guess was higher or lower than the secret number. If they run out of guesses
    they lose, but if they guess the correct number they win. 

    Python Version Required: 3.11.X

    Author: Noah Chaney
"""


def main():
    """
        This section prompts the user to select a difficulty for the game
        Easy: Range 1-10, 3 guesses
        Medium: Range 1-100, 5 guesses
        Hard: 1-1000, 7 guesses
    """
    print("\nWelcome to the Hi-Lo Game!")
    print("--------------------------\n")
    diff = 0
    while diff == 0:
        userIn = input("Choose Difficulty - 1=Easy, 2=Medium, 3=Hard: ")
        try:
            difficulty = int(userIn)
            if difficulty > 3 or difficulty < 1:
                breaker = int("s") # this is purely to throw an error so it goes to the except block
            else:
                diff = difficulty
        except:
            print("Invalid difficulty, try again!")


    """
        This section sets the parameters outlined from respective
        difficulty chosen
    """
    guessingNum = 0
    numGuesses = 0
    hi = 0
    match diff:
        case 1:
            guessingNum = randint(1, 10)
            numGuesses = 3
            hi = 10
        case 2: 
            guessingNum = randint(1, 100)
            numGuesses = 5
            hi = 100
        case 3:
            guessingNum = randint(1, 1000)
            numGuesses = 7
            hi = 1000


    """
        Main loop for the game. Takes user input number and determines if the guess was high or low
        Each valid guess takes away one guess count, when it reaches 0 the game ends. If the guess isn't
        valid no guess count is removed. If guess is correct you win. Prompts to restart game or end if fail
        or win. If player guesses -1 at any point the gamne will end
    """
    while True:
        print("Guess a number between 1 and",hi,", enter -1 to leave\n")
        print("Guesses left: ", numGuesses)

        try:
            guess = int(input("Guess: "))

            if guess == -1:
                break

            if numGuesses > 1 and guess != guessingNum:
                if guess > guessingNum:
                    print("Guess is high")
                    numGuesses -= 1
                elif guess < guessingNum:
                    print("Guess is low")
                    numGuesses -= 1
                
            else:
                if guess == guessingNum:
                    print("Correct! You win!")
                    break

                print("You've ran out of guesses! You Lose!")
                break

        except:
            print("Invalid guess, try again!")

    print("\nThanks for playing!\n")

if __name__ == "__main__":
    main()