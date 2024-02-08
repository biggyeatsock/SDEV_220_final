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


# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists



def redata():
    data =  open('data.txt', 'r') # reads the data from the file
    for line in data:
        print(f'\n{line}')


def write_info(data): # writes the info to the file.
    wcheck = input("Would you like to write to the file? (y/n) \n > ")
    if wcheck == "y":
        uinput = input("What would you like to write to the file? \n > ")
        data.write(uinput)
    elif wcheck == "n":
        print("\nOkay, no changes made.\n")
    return data



def main(): # Main function that runs the program.
    print("Welcome to the BookWise Book Manager")
    redata() # reads the data from the file
    
    # write_info(data)
    # print(data)



if __name__ == '__main__': # Allows you to run it as a script and not be ran if imported.
    main()
