"""
Name: Atlas Mallams
Class Section: 0018
Program 2 Code
Creation Date: September 19, 2023
Due Date: September 24, 2023
"""

# TODO: Add documentation comments to code

""" OPERATION COUNT VARIABLES """
add_count = 0
subtract_count = 0
multiply_count = 0
divide_count = 0

""" FUNCTIONS """
def print_display_menu():
    """Prints list of available operations with their corresponding selection number."""
    print('\n1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exit\n')


def print_total_operations():
    """Computes and prints the total amount of operations. Also prints how many times each operation was used as long
    as it was used once."""
    operation_count = add_count + subtract_count + multiply_count + divide_count # Adds up all operation totals
    print(f'\nYou had {operation_count} arithmetic operations as below:')
    if add_count > 0:
        print(f'"+" : {add_count}')
    if subtract_count > 0:
        print(f'"-" : {subtract_count}')
    if multiply_count > 0:
        print(f'"*" : {multiply_count}')
    if divide_count > 0:
        print(f'"/" : {divide_count}')
    if add_count == subtract_count == multiply_count == divide_count == 0:  # Runs only if no operations were performed
        print(f'No operations.')

    print('\nExiting the calculator. Goodbye!')


def ask_new_calculation():
    """Asks the user if they would like to perform another operation, and returns the corresponding boolean value."""
    perform_new_calc = input('\nDo you want to perform another calculation? (y/n): ').lower()

    # Continues to prompt the user until y or n is entered
    while perform_new_calc != 'y' and perform_new_calc != 'n':
        perform_new_calc = input('Invalid choice, please select (y/n): ')
    if perform_new_calc == 'y':
        return True
    else:
        return False


def get_user_operation():
    """Allows the user to select which operation they want to perform."""
    print_display_menu()
    answer_choice = int(input('Please select an operation (1-5): '))
    # Runs until the user enters a valid number
    while not (0 < answer_choice < 6):
        print('Invalid choice. Please select a valid operation.\n')
        answer_choice = int(input('Please select an operation (1-5): '))
    return answer_choice


def add(num1, num2):
    """Returns the sum of num1 and num2"""
    return num1 + num2


def subtract(num1, num2):
    """Returns the difference of num1 and num2"""
    return num1 - num2


def multiply(num1, num2):
    """Returns the product of num1 and num2"""
    return num1 * num2


def divide(num1, num2):
    """Returns the quotient of num1 divided by num2"""
    return num1 / num2


""" MAIN CODE """
print('Welcome to the Simple Calculator!')

while True:  # Loop runs until terminated by a break statement
    operation = get_user_operation()

    # Calls functions based on which operation the user selected
    if operation == 1:  # Add
        add_count += 1
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        print(f'Result: {num1:.1f} + {num2:.1f} = {add(num1, num2):.2f}')
    elif operation == 2:  # Subtract
        subtract_count += 1
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        print(f'Result: {num1:.1f} - {num2:.1f} = {subtract(num1, num2):.2f}')
    elif operation == 3:  # Multiply
        multiply_count += 1
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        print(f'Result: {num1:.1f} * {num2:.1f} = {multiply(num1, num2):.2f}')
    elif operation == 4:  # Divide
        divide_count += 1
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        while num2 == 0:  # Check if num2 would cause divide by zero error
            print('Error: Division by zero is not allowed.')
            num2 = int(input('Enter the second number: '))
        print(f'Result: {num1:.1f} / {num2:.1f} = {divide(num1, num2):.2f}')
    elif operation == 5:  # Exit
        break

    # Calls the function to ask user if they would like to do another calculation
    new_calc = ask_new_calculation()

    # Ends while loop if new_calc value is False
    if not new_calc:
        break

print_total_operations()  # Prints the amount of operations summary before the program ends
