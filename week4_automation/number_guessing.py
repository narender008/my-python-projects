import random

guessed_number = input("please guess any number(between zero to 10): ")

guessed_number = int(guessed_number)


random_number = random.randint(0, 10)


while guessed_number <= 10:
    if guessed_number == random_number:
        print("you have guessed it correctly !")
        print(f" guessed number is {random_number}")
    else:
        print("try again")
    exit()

print("you have entered wrong range")
