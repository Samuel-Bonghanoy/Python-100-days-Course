import random

def guess_num(lives_left):
    print(f"You have {lives_left} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    return guess

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower() #asks the user to input a difficulty level

#sets user lives to 5 or 10 depending on the difficulty
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5

number_to_guess = random.randint(1, 100)
guess = 0
while not guess == number_to_guess:
    if lives > 0:
        while lives > 0:
            guess = guess_num(lives)
            if guess != number_to_guess:
                if guess > number_to_guess:
                    print("Too High.")
                elif guess < number_to_guess:
                    print("Too low.")
                lives -= 1
                print("Guess again.")
            elif guess == number_to_guess:
                print(f"The correct number was {number_to_guess}, and you got it right! You win!")
                break
    if lives == 0:
        print(f"The correct number was {number_to_guess}.")
        print("You ran out of lives.")
        print("You lose.")
        break
