def calculator_interface_start():

    # Take input from user
    calc_query = input('''
Do you want to calculate?
Please type Y for YES or N for NO.
''')

    # If user types Y, run the calculate() function
    if calc_query == 'Y':
        calculate()

    # If user types N, say good-bye to the user and end the program
    elif calc_again == 'N':
        print('See you later.')

    # If user types another key, run the function again
    else:
        calculator_interface_start()

def calculate():
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)
  