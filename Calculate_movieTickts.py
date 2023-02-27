
print("WELCOME, Enter age to get tickets price.")
print("Enter 'q' for ending program")
print("====================================================")
ticket_price = 100

while True:
    age = input("Enter Your Age.")
    
    if age.lower() == 'q':
        break
    else:
        if age.isdigit():
            age = int(age)
            if age <= 3 and age >=1:
                print("Tickets Amaount is Zero!")
            elif age <= 100 and age>=1:
                print(f"The Ticket Amaount is {ticket_price}")
            elif 4 < age <=12:
                print(f"Tickets Amount is {ticket_price/2}!")
            else:
                print("please enter valid age")
        else:
            print(f"Please Enter Valid age. Given age is {age}")