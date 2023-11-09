"""
Name: Atlas Mallams
Class Section: 0018
Program 5 Code
Creation Date: November 8, 2023
Due Date: November 19, 2023
"""
""" BOOK CLASS """


class Book:
    book_collection = []  # Empty list for storing books

    def __init__(self, title='none', author='none', year=0, isbn='none', is_available=True):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.is_available = is_available

    def get_book_info(self):
        """Returns the title, author, year, and ISBN for the book passed as an argument"""
        return [self.title, self.author, self.year, self.isbn]

    def check_availability(self):
        """Checks the availability of a specific book (if the book exists in the collection)"""
        for book in self.book_collection:
            if book.title == self.title and book.author == self.author:
                if book.is_available:
                    return f'The book \'{title}\' by {author} is available.\n'
                else:
                    return f'The book \'{title}\' by {author} is not available.\n'
        return 'Book could not be found in the collection.\n'

    def add_book(self):
        """Adds a new book or updates the value of is_available to True for preexisting ones"""
        for book in self.book_collection:
            if book.get_book_info() == self.get_book_info():
                book.is_available = True
                return f'The book \'{self.title}\' has been added to the collection.\n'
        self.book_collection.append(self)
        return f'The book \'{self.title}\' has been added to the collection.\n'

    def checkout(self):
        """Checks out a book (if a valid book) by setting the is_available variable to False"""
        for book in self.book_collection:
            if book.get_book_info() == self.get_book_info():
                book.is_available = False
                return f'The book \'{self.title}\' has been removed from the collection.\n'
        return f'The book \'{self.title}\' could not be found in the collection.\n'

    def print_collection(self):
        """Prints the available books in the collection"""
        print('Available Books:')
        if len(self.book_collection) == 0:
            print('Book collection is empty.')
        else:
            available_book = False
            for book in self.book_collection:
                if book.is_available:
                    print(f'{book.title} by {book.author}')
                    available_book = True
            if not available_book:
                print('There are no available books in the collection.')
        print()


""" VARIABLES """
menu = {
    '1': "Add or return a book to the collection",
    '2': "Check out a book from the collection",
    '3': "Check book availability",
    '4': "Print available books in the collection",
    'Q': "Quit"
}


""" FUNCTIONS """


def print_menu():
    """Prints the menu options with the corresponding selector values"""
    print('=' * 42)
    print(f'{"Menu":^42}')
    print('=' * 42)
    for menu_id, menu_option in menu.items():
        print(f'{menu_id}. {menu_option}')
    print()


def input_book_info():
    """Collects book info from a user and returns a Book with the given inputs"""
    title = input('Enter the title: ')
    author = input('Enter the author: ')
    while True:
        try:
            year = int(input('Enter the year: '))
            break
        except ValueError:
            print('Invalid year input! Please try again.')
    isbn = input('Enter the ISBN: ')
    print('')
    return Book(title, author, year, isbn)


""" MAIN PROGRAM """
while True:
    print_menu()
    menu_choice = input('Enter your choice: ').upper()
    while menu_choice not in menu:
        print('Invalid menu choice! Please try again.\n')
        menu_choice = input('Enter your choice: ').upper()
    print()

    if menu_choice == 'Q':  # Stops the program
        break

    elif menu_choice == '1':  # Adds book to collection
        print(input_book_info().add_book())

    elif menu_choice == '2':  # Removes book from collection
        print(input_book_info().checkout())

    elif menu_choice == '3':  # Checks the availability of a specific book in the collection
        title = input('Enter the title: ')
        author = input('Enter the author: ')
        print(Book.check_availability(Book(title, author)))

    elif menu_choice == '4':  # Prints available book in the collection
        Book.print_collection(Book())
