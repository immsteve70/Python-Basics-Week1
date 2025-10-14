import random

secret_num = random.randint(1, 20)
attempts = 0

while True:
    attempts += 1
    action = int(input("Guess a number between 1 - 20: "))

    if action > secret_num:
        print("Too High!")
    elif action < secret_num:
        print("Too Low!")
    else:
        print("You got it!")
        break


print(f"You made {attempts} attempts!")
