import random

print("🎯 Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100. Can you guess it?")

# generate random number
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7   # limit tries

while attempts < max_attempts:
    guess = int(input(f"\nAttempt {attempts+1}/{max_attempts} - Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"🎉 Congratulations! You guessed it in {attempts} tries.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

if guess != secret_number:
    print(f"\n😢 Sorry! The number was {secret_number}. Better luck next time!")
