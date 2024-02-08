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
from pathlib import Path


FILE_PATH = "data.txt"



def read_info(): # opens the file and reads the info, within.
    data = Path(__file__).with_name(FILE_PATH)
    with data.open(mode='r') as file:
        data = file.read()
    return data.split("\n")


def main(): # Main function that runs the program.
    print("Welcome to the BookWise Book Manager")
    data = read_info()
    print(data)


if __name__ == '__main__': # Allows you to run it as a script and not be ran if imported.
    main()
