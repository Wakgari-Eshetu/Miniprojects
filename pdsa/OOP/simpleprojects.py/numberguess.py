print("Jesus is lord and wellcome the number guessing game.")

import random

lower = int(input("Enter the lower number:"))
upper = int(input("Enter the upper number:"))

num = random.randint(lower,upper)

how_many_time = int(input("Enter the number of  times you want to guess:"))

j = how_many_time
i = 0
while i<j:
    i+=1
    guess = int(input("Enter your guess:"))

    if guess == num:
        print(f"Correct guess!! you guessed it in the {i} attempts.")
        break
    elif i >= j and guess != num:
        print(f'Sorry! The number was {num}. Better luck next time.')
    elif guess > num:
        print("Your guess was greater.")
    elif guess<num:
        print("Your guess was less.")
