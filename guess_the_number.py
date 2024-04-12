from random import randint

random_number = int(randint(1, 100))


print('#Guess the number Game#\n', 'Your goal is to guess the number\n', 'From 1 to 100\n', 'Good luck')


while True:
    number = input("Guess the number : ")
    if number.isnumeric():
        number_int = int(number)
        if number_int == random_number:
            print("You win!")
            break
        elif number_int <= random_number:
            print("Too small")
            continue
        elif number_int >= random_number:
            print("Too big")

    else:
        print("It's not a number")
        continue
