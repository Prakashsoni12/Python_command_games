
#this function will return square of each numbers
def square_pattrns(n):
    pattern_list = [i**2 for i in range(1,n+1)]
    return pattern_list

#add square to previous one
def add_square_pattrns(n):
    pattern_list = []
    x = 1
    for i in range(1,n+1):
        pattern_list.append(x)
        x = x + i**2
    return pattern_list

#add square to previous one plus one
def add_square_plus_one_pattrns(n):
    pattern_list = []
    x = 1
    for i in range(1,n+1):
        pattern_list.append(x)
        x = x + i**2 + 1
    return pattern_list

#this function will return cube of each numbers
def cube_pattern(n):
    pattern_list = [i**3 for i in range(1,n+1)]
    return pattern_list

def add_cube_plus_one_pattrns(n):
    pattern_list = []
    x = 1
    for i in range(1,n+1):
        pattern_list.append(x)
        x = x + i**3 + 1
    return pattern_list

def add_odd_pattrns(n):
    pattern_list = []
    x = 2
    odd_list = [i for i in range(1,n*2+1) if i%2==1]
    for i in range(1,n+1):
        pattern_list.append(x)
        x = x + odd_list[i-1]
    return pattern_list

while True:
    print("==============================================") 
    print("Select from series to print.")
    print("Pattern 1. Square Numbers. ")
    print("Pattern 2. Add Square Numbers to previous numbers. ")
    print("Pattern 3. Add Square plus one to previous Numbers. ")
    print("Pattern 4. Cube Numbers. ")
    print("Pattern 5. Add cube plus one to previous Numbers. ")
    print("Pattern 6. Add odd Numbers to previous numbers. ")
    print("==============================================") 

    pattern_option = input("Enter Options: ")

    if pattern_option.isdigit() and int(pattern_option) in range(1,7):
        num_element = input("Enter required element in pattern: ")
        if num_element.isdigit():
            num_element = int(num_element)
            if pattern_option == '1':
                p_list = square_pattrns(num_element)
                print(p_list)

            elif pattern_option == '2':
                p_list = add_square_pattrns(num_element)
                print(p_list)
            elif pattern_option == '3':
                p_list = add_square_plus_one_pattrns(num_element)
                print(p_list)
            elif pattern_option == '4':
                p_list = cube_pattern(num_element)
                print(p_list)
            elif pattern_option == '5':
                p_list = add_cube_plus_one_pattrns(num_element)
                print(p_list)
            elif pattern_option == '6':
                p_list = add_odd_pattrns(num_element)
                print(p_list)

            is_continue = input("Do you want to continue?(yes/no). ")
            if is_continue.lower() == 'yes':
                continue
            else:
                break
        else:
            print(f"Required Options are 1,2,3,4,5,6 But Recived '{num_element}' ")

    else:
        print(f"**Expected options must be positive number in range of (1,2,3,4,5,6) but recevied '{pattern_option}' ")
        print("Please choose the option again.")
        continue
