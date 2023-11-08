"""
Name: Atlas Mallams
Class Section: 0018
Program 4 Code
Creation Date: October 18, 2023
Due Date: October 29, 2023
"""


""" IMPORTS """
import csv
import random

""" VARIABLES """
menu = {
    1: 'Search by Name',
    2: 'Calculate Average Salary',
    3: 'Save and Exit'
}

input_lines = []
first_input_line = []

""" FUNCTIONS """


def read_file(in_name):
    first_time = True
    with open(in_name, 'r') as input_file:
        csv_reader = csv.reader(input_file)
        for row in csv_reader:
            if first_time:
                first_input_line.extend(row)
                first_time = False
                continue
            input_lines.append(row)
    write_file()


def write_file():
    with open('output_data.csv', 'w') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(first_input_line)
        for line in input_lines:
            csv_writer.writerow(line)


def create_status_col():
    first_input_line.append('Status')
    for line in input_lines:
        if int(line[1]) >= 25:
            line.append('Adult')
        else:
            line.append('Young')
    write_file()
    display_status()


def create_salary_col():
    first_input_line.append('Salary')
    for line in input_lines:
        line.append(random.randint(30000, 100000))
    write_file()


def calc_average_age():
    average_age = 0
    for line in input_lines:
        average_age += int(line[1])
    print(f'\nAverage age: {average_age / len(input_lines):.2f}')


def calc_average_salary():
    average_salary = 0
    for line in input_lines:
        average_salary += int(line[4])
    return average_salary / len(input_lines)


def display_status():
    adult_count = 0
    young_count = 0
    for line in input_lines:
        if line[3] == 'Adult':
            adult_count += 1
        else:
            young_count += 1
    print(f'Number of adult individuals: {adult_count}')
    print(f'Number of young individuals: {young_count}')


def lookup_person(name):
    found_person = False
    for line in input_lines:
        if line[0] != name:
            continue
        else:
            found_person = True
            count = 0
            print('\nSearch Result:')
            for item in line[:-1]:
                print(f'{first_input_line[count]}: {item}')
                count += 1
    if not found_person:
        raise KeyError


def display_menu():
    print(f'\n{"Menu Options":^27}')
    print(f'{"":=^27}')
    for num, item in menu.items():
        print(f'{num}. {item}')
    print()


""" MAIN PROGRAM """
# Asks the user for the input file name and reads the file (when valid)
while True:
    input_filename = input('Enter input file name ==> ')
    try:
        read_file(input_filename)
        break
    except FileNotFoundError:
        print('Invalid file name. Please enter a valid file.\n')
    except IOError:
        print('There was an error processing the chosen file.\n')

calc_average_age()
create_status_col()
create_salary_col()

# Allows user to perform functions until loop is terminated
while True:
    display_menu()
    try:
        menu_choice = int(input('Enter your choice ==> '))
    except ValueError:
        print('Invalid answer format. Please enter an integer.')
        continue

    if menu_choice not in menu.keys():
        print('Invalid choice. Please enter a valid option.')
        continue

    if menu_choice == 1:
        lookup_name = input('\nEnter the name to search for ==> ')
        try:
            lookup_person(lookup_name)
        except KeyError:
            print(f'No person with the name {lookup_name} found.')
    elif menu_choice == 2:
        print(f'\nAverage salary: ${calc_average_salary():.2f}')
    else:
        print('\nData saved to \'output_data.csv\'. Exiting...')
        break
