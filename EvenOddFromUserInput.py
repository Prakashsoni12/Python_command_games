'''
option1. Print the list of even numbers upto nth term.
option2. Print the list of odd numbers upto nth term.
option3. Tell the user if number is even or odd.
option4. Run the project in loop until user enter 'End'
'''
import colorama
from colorama import Fore
while True:
    print(Fore.WHITE+"=================================================")
    print(Fore.RED+"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(Fore.WHITE+"=================================================")
    print(Fore.YELLOW+"Option 1. Print a list of even numbers upto nth term.")
    print(Fore.YELLOW+"Option 2. Print a list of odd numbers upto nth term.")
    print(Fore.YELLOW+'Option 3. Tell User if a number is even or odd.')
    print(Fore.YELLOW+"Enter 'end' to quit the programm.")
    print(Fore.WHITE+"=================================================")
    print(Fore.RED+"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(Fore.WHITE+"=================================================")
    user_op = input(Fore.BLUE+"Select an option: ")

    if user_op.lower() == 'end':
        break
    else:
        if user_op.isdigit():
            user_op = int(user_op)
            if user_op == 1:
                nth_term = int(input("Required Number of Elemnts: "))
                even = [i for i in range(1, nth_term*2+1) if i%2==0]
                print(even)
            elif user_op == 2:
                nth_term = int(input("Required Number of Elemnts: "))
                odd_num = [i for i in range(1, nth_term*2+1) if i%2==1]
                print(odd_num)
            elif user_op == 3:
                even_odd_num = int(input("Enter Number To Check Even or Odd: "))
                if even_odd_num%2==0:
                    print(Fore.WHITE+f"{even_odd_num} is a Even number.")
                else:
                    print(Fore.WHITE+f"{even_odd_num} is a Odd number.")
            else:
               print(Fore.GREEN+"Choose the correct options.")
        else:
            print(Fore.RED+f"Given input must be positive number but got{user_op}.")