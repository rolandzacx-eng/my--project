import random
secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")
guess = 0
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print ("Too High! Try again.")
print("congratulations! You guessed the number!")    
