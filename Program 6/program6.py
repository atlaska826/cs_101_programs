"""
Name: Atlas Mallams
Class Section: 0018
Program 6 Code
Creation Date: November 28, 2023
Due Date: December 9, 2023
"""

""" ------------ """
""" ANIMAL CLASS """
""" ------------ """


class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def display_info(self):
        print(f'{self.name} - Age: {self.age}, Species: {self.species}', end='')


""" ------------ """
""" MAMMAL CLASS """
""" ------------ """


class Mammal(Animal):
    def __init__(self, name, age, species, fur_color):
        Animal.__init__(self, name, age, species)
        self.fur_color = fur_color
        self.health_status = "Healthy"

    def get_health_status(self):
        return self.health_status

    def set_health_status(self, status):
        self.health_status = status

    def display_info(self):
        Animal.display_info(self)
        print(f', Fur Color: {self.fur_color}, Health: {self.health_status}', end='')


""" --------- """
""" ZOO CLASS """
""" --------- """


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal_name):
        for animal in self.animals:
            if animal.name == animal_name:
                self.animals.remove(animal)
                break

    def display_zoo_info(self):
        print(f'Zoo: {self.name}\n')
        if len(self.animals) > 0:
            for animal in self.animals:
                animal.display_info()
                print()
            print()


""" ------------ """
""" MAIN PROGRAM """
""" ------------ """

menu = {
    '1': 'Add a mammal to the zoo',
    '2': 'Remove a mammal from the zoo',
    '3': 'Display information about the entire zoo',
    '4': 'Exit the program'
}


def display_menu():
    print('Zoo Management System Menu:')
    for num, desc in menu.items():
        print(f'{num}. {desc}')


""" BASE CODE """
zoo = Zoo('Comp Sci Zoo')

while True:
    display_menu()
    menu_choice = input('Enter your choice (1-4): ')
    while menu_choice not in menu:
        print('Invalid choice. Please enter a number between 1 and 4.\n')
        display_menu()
        menu_choice = input('Enter your choice (1-4): ')
    print()
    choice = int(menu_choice)

    if choice == 4:
        break

    elif choice == 1:
        name = input('Enter the name of the mammal: ').title()

        while True:
            try:
                age = int(input('Enter the age of the mammal: '))
                if age < 0:
                    print('Age must be greater than or equal to 0.')
                    continue
                break
            except ValueError:
                print('Age must be a number.')

        species = input('Enter the species of the mammal: ').title()
        fur_color = input('Enter the fur color of the mammal: ').title()

        zoo.add_animal(Mammal(name, age, species, fur_color))
        print(f'{name} was added to {zoo.name}.\n')

    elif choice == 2:
        if len(zoo.animals) == 0:
            print('There are no animals to remove.\n')
            continue
        animal_name = input('Enter the name of the animal to remove: ').title()
        if animal_name not in [animal.name for animal in zoo.animals]:
            print('Animal could not be found.\n')
        else:
            zoo.remove_animal(animal_name)
            print(f'{animal_name} was removed from {zoo.name}.\n')

    elif choice == 3:
        zoo.display_zoo_info()

print('Exiting Zoo Management System. Goodbye!')
