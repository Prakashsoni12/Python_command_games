'''
Game 1: play Copy Cat.
Game 2: Play Madlib.
'''
#madlibs are short amusing stories made up by taking fwe inputs from someone.
#After placing those inputs in a pre-written story.

import colorama
from colorama import Fore
while True:
    print(Fore.LIGHTYELLOW_EX+"==================================================")
    print("Game 1: Play Copy Cat.")
    print("Game 2: Play Madlib.")
    print("Enter 'q' to end the program.")
    print(Fore.LIGHTYELLOW_EX+"==================================================")
    
    user_option = input("Select a game to play: ")
    
    if user_option.lower()=='q':
        break
    else:
        if user_option.isdigit():
            user_option = int(user_option)
            if user_option == 1:
                print("I am Copy cat! I will repeat whatever you type. ")
                print("I am Copy cat! I will repeat whatever you type. ")
                print("Enter 'q' to end the program.")
                while True:
                    text = input(Fore.LIGHTBLUE_EX+"What do you have to say: ")
                    if text.lower() == 'q':
                        break
                    else:
                        print(f"{text.upper()}!!!")

            elif user_option == 2:
                print("A magic book madlib game. Give inputs, Read Story, Enjoy!!!.")
                while True:
                    name1 = input(Fore.LIGHTGREEN_EX+"Enter any name: ")
                    name2 = input(Fore.LIGHTGREEN_EX+"ENter another name: ")
                    color = input(Fore.LIGHTGREEN_EX+"Enter any color: ")
                    new_old = input(Fore.LIGHTGREEN_EX+"Enter new/old: ")
                    emotion = input(Fore.LIGHTGREEN_EX+"Enter an emotion: ")
                    place = input(Fore.LIGHTGREEN_EX+"Enter any place: ")

                    a_magic_book = Fore.LIGHTRED_EX+f'''
                    {name1.title()} found a {color} book inside {new_old} trunk.
                    He called {name2.title()}. They wanted to check the book but
                    {name2.title()} stopped him, because he was very {emotion}.

                    In the night {name1.title()} thought it would be nice if
                    he went to {place.title()} and read that book. Next morning,
                    to his {emotion} he found himself in {place.title()},
                    with that {color} book.
                    '''
                    print(a_magic_book)
                    is_continue = input(Fore.LIGHTMAGENTA_EX+"Do you want to continue? (yes/no): ")
                    if is_continue.lower == 'q':
                        continue
                    else:
                        break
            else:
                break
        else: 
            print(f"Please input the positive digits only, but got{user_option}")




