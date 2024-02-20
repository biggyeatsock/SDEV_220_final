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


def redata(): # Read the data from the file
    data =  open('data.txt', 'r') 
    for line in data:
        print(f'\n{line}')
    return data


def write_info(data): # writes the info to the file.
    data = open('data.txt', 'a') # opens the file for appending.
    wcheck = input("Would you like to write to the file? (y/n) \n > ")
    if wcheck == "y":
        uinput = input("What would you like to write to the file? \n > ")
        try:
            if len(uinput) != 0: # Checks if the user wrote anything.
                print(f"\nWriting to the file...\n")
                data.write('\n'+uinput) # Writes the user input to the file.
            else: # Prints the error
                raise ValueError("You didn't write anything, so no changes made.")
        except ValueError as e:
            print(e)
    else:
        print("\nOkay, no changes made.\n")

def userclose():
    uinput = input("Would you like to close the program? (y/n) \n > ")
    if uinput == "y":
        print("Closing the program...")
        exit()


def main(): # Main function that runs the program.
    print("Welcome to the BookWise Book Manager")
    while True: # Loops the Program.
        data = redata() # reads the data from the file
        write_info(data)
        userclose()




if __name__ == '__main__': # Allows you to run it as a script and not be ran if imported.
    main()
