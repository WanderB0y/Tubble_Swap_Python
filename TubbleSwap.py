first_name = input("Enter your first name :: ")
last_name = input("Enter your last naame :: ")

fullname = "Fullname :: " + first_name.title() + " " + last_name.title()

print(fullname)

flow = True

while flow:

    print("Y - Yes")
    print("N - No")
    var_swap = input("Would you want to swap it :: ")

    if var_swap == 'Y':
        first_name, last_name = last_name, first_name
        print("Your fullname has been change")
        print(fullname)
        flow = False
    elif var_swap == 'N':
        print("Your fullname has not been change")
        


