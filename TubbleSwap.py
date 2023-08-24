first_name = input("Enter your first name :: ")
last_name = input("Enter your last name :: ")

first_fullname = "\n" + "Fullname :: " + first_name.title() + " " + last_name.title() + "\n"

print(first_fullname)


#Controlling thee loop using boolean
flow = True

while flow:
    print("Would you want your first name and last name to change position\n")
    print("Press Y - Yes")
    print("Press N - No\n")
    var_swap = input("Enter Your Choice :: ")

    if var_swap == 'Y':
        #Changing the value of two variables without using temporary variable
        first_name, last_name = last_name, first_name
        new_fullname = "\n" + "Fullname :: " + first_name.title() + " " + last_name.title() + "\n"

        #Print it again
        print("\nYour fullname has been change")
        print(new_fullname)
        #Controlling the loop using boolean
        flow = False

    elif var_swap == 'N':
        print("\nYour fullname remains unchange")
        print(first_fullname)
        #Controlling the loop using boolean
        flow = False

    else:
        print("\nYour input is incorrect please try again\n")

print("Thank you " + first_name + " for using our program")
        


