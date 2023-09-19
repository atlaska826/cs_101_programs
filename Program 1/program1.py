"""
Name: Atlas Mallams
Class Section: 0018
Program 1 Part 1
Creation Date: August 28, 2023
Due Date: September 10, 2023
"""

# User input prompts
user_name = input('Enter your name: ')
user_age = int(input('Enter your age: '))
c_temperature = float(input('Enter the temperature (in Celsius): '))

f_temperature = (c_temperature * (9/5)) + 32
user_age_dog_years = user_age * 7

# Personalized greeting
print(f'\nHello {user_name}!\n')
print(f'Here are your results:')

# Print results
print(f'Temperature in Fahrenheit: {f_temperature} F')
print(f'Your age in human years: {user_age} years')
print(f'Your age in dog years: {user_age_dog_years} dog years')
