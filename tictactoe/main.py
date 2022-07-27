
def userChoice():
    # digit, range
    acceptance_range = range(0, 10)
    isInAcceptanceRange = False
    input_str = 'False'

    while input_str.isdigit() == False or isInAcceptanceRange == False:
        input_str = input("Enter a number in 0 to 10")

        if input_str.isdigit() == False:
            print('Not a digit, please enter a digit')

        if input_str.isdigit() == True:
            if int(input_str) in acceptance_range:
                isInAcceptanceRange = True
            else:
                print('Not in the range of 0 to 10')
                isInAcceptanceRange = False

    return int(input_str)

userChoice()
