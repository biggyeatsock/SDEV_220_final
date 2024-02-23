#####################
#   A Library book manager
#  
#   Project name: BookWise Book Manager
#   
#   
#
#
#
#####################

from classes.coolstuff import view, Model
import os
from os.path import isfile, getsize
file_path = 'database.py'

def database_info(): # gathers info about the database.
    import sqlite3
    try:
        if not isfile('books.db'): # if the database is not found, it will create a new one. 
            raise sqlite3.OperationalError
        if isfile('books.db'): # if a database is present it gives you the size
            print(f'\nDatabase file size: {getsize("books.db")} bytes')
    except sqlite3.OperationalError as e:
        print(f'File Not Found')
        print('Creating a database.....')
        create_database(file_path)

def create_database(file_path): # Create a database if one hasn't been made
    try:
        if not isfile(file_path):
            raise FileNotFoundError
        elif isfile(file_path):
            os.system(f'python {file_path}')
    except FileNotFoundError:
        print(f'Error: the file {file_path} does not exist.')
        exit()

def userclose(): # Closes on user command.
    uinput = input("\nWould you like to close the program? (y/n) \n> ")
    if uinput == "y":
        print("Closing the program...")
        exit()

def main(): # Main function that runs the program.
    database_info() # Prints if the database creation file has been ran.
    print("\nWelcome to the BookWise Book Manager\n")
    while True:
        print("What would you like to do?")
        print("1. Write to the database")
        print("2. Read from the database")
        print("3. Close the program.")
        uinput = input("> ")
        my_model = Model()
        my_view = view(my_model)
        if uinput == "1": # Add books into the database
            addbook = input("\nWhat is the name of the book? \n> ")
            addauthor = input("\nWhat is the name of the author? \n> ")
            addgenre = input("\nWhat is the genre of the book? \n> ")
            addyear = input("\nWhat is the year of publication? \n> ")
            my_model.add_data(addbook, addauthor, addgenre, addyear) # Sends the data over into the class file.
        elif uinput == "2":    
            my_view.show_data()
            print("\n")
        elif uinput == "3":
            userclose()
        else:
            print("Invalid input, try again.")




if __name__ == '__main__': # Allows you to run it as a script and not be ran if imported.
    main()
