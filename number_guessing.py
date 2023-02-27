import random

number = random.randint(1,100)

print("HELLO, Welcome to the Number guessing game.")
print("I have Numbers between 1 to 100")
print("You have 8 tries to complete the game.")
print("Lets's Play!!!")
print("+___-_________-___________-________-_______-_______+")

try_count = 0
while try_count <8:
    user_guess = input("Enter Your Guessing Number!")

    try:
        user_guess = int(user_guess)
    except Exception as ep:
        print(ep)
        print(f"Sorry couldn't understant that. input must be a number")
        continue
    try_count +=1

    if 1<= user_guess <= 100:
        if user_guess == number:
            print("Congratulations, YOU WINNER!!!")
            start_again = input("Do you want to continue(yes/no).")
            if start_again.lower() == 'yes':
                try_count = 0
                continue
            else:
                break
        elif user_guess>number:
            print("The number you have enterd is GREATER")
            print(f"You left with {8-try_count} tries")
        elif user_guess<number:
            print("The number you have enterd is SMALLER")
            print(f"You left with {8-try_count} tries")

    elif user_guess > 100:
        print(f"SORRY, You have enterd {user_guess}, its more then limit")
        print(f"You left with {8-try_count} tries")

    else:
        print(f"Required a positive number nut got {user_guess}")
        print(f"You left with {8-try_count} tries")

    if try_count == 8:
        print(f"Oops, You have tried {try_count} times.")
        print(f"The Correct number is {number}")
        print("Better luck next time")
        break