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



def userclose():
    uinput = input("\nWould you like to close the program? (y/n) \n> ")
    if uinput == "y":
        print("Closing the program...")
        exit()


def main(): # Main function that runs the program.
    print("Welcome to the BookWise Book Manager")
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
