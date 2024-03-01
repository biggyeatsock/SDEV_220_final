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

"""
def main(): # Main function that runs the program.
    database_info() # Prints if the database creation file has been ran.
    print("\nWelcome to the BookWise Book Manager\n")
    while True:
        print("What would you like to do?")
        print("1. Write to the database")
        print("2. Removes books from database")
        print("3. Shows all the books")
        print("4. Close the program.")
        uinput = input("> ")
        my_model = Model()
        my_view = view(my_model)
        if uinput == "1": # Add books into the database
            addbook = input("\nWhat is the name of the book? \n> ")
            addauthor = input("\nWhat is the name of the author? \n> ")
            addgenre = input("\nWhat is the genre of the book? \n> ")
            addyear = input("\nWhat is the year of publication? \n> ")
            my_model.add_data(addbook, addauthor, addgenre, addyear) # Sends the data over into the class file.
        elif uinput == "2": # Removes books from database
            bookid = input("\nWhat is the ID of the book? \n> ")
            my_model.remove_data(bookid) # Sends the data over into the class file.
            print("Removal successful!!")
        elif uinput == "3": # Prints all the books in the database  
            my_view.show_data()
            print("\n")
        elif uinput == "4":
            userclose()
        else:
            print("Invalid input, try again.")
"""


import tkinter as tk

class BookWindow:
    def __init__(self, root, num_books):
        self.root = root
        self.root.title("Book List")

        self.canvas = tk.Canvas(root, width=400, height=300, bg='white')
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        my_model = Model()
        my_view = view(my_model)
        self.num_books = num_books
        self.rectangles_data = [{'text': my_model.get_row(i), 'color': 'red'} for i in range(self.num_books)]

        self.draw_centered_rectangles()

    def draw_centered_rectangles(self):
        num_columns = 3  # Number of columns in each row
        rect_width = 100
        rect_height = 50

        for index, data in enumerate(self.rectangles_data):
            # Calculate the row and column numbers
            row = index // num_columns
            col = index % num_columns

            # Calculate the coordinates for the centered rectangle
            x1 = (self.canvas.winfo_reqwidth() - rect_width * num_columns) // 2 + col * rect_width
            y1 = (self.canvas.winfo_reqheight() - rect_height * (num_columns + 1)) // 2 + row * rect_height
            x2 = x1 + rect_width
            y2 = y1 + rect_height

            # Draw the rectangle
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=data['color'], outline='black')

            # Calculate the text coordinates for centering
            text_x = (x1 + x2) / 2
            text_y = (y1 + y2) / 2

            # Draw the text
            self.canvas.create_text(text_x, text_y, text=data['text'], fill='white', font=('Helvetica', 6, 'bold'))

class AddWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Add books")

        self.text_widget = tk.Text(root, height=1, width=10)
        self.text_widget.pack(pady=10)
        self.text_widget.insert(tk.END, "Book name:")
        self.text_widget = tk.Text(root, height=1, width=10)
        self.text_widget.pack(pady=10)
        self.text_widget.insert(tk.END, "Book author:")
        self.text_widget = tk.Text(root, height=1, width=10)
        self.text_widget.pack(pady=10)
        self.text_widget.insert(tk.END, "Book genre:")
        self.text_widget = tk.Text(root, height=1, width=10)
        self.text_widget.pack(pady=10)
        self.text_widget.insert(tk.END, "Book year:")
        add_button = tk.Button(root, text="Add book", command=self.open_books_window) #add books command
        add_button.pack(pady=10)
        

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Main")



        self.text_widget = tk.Text(root, height=1, width=26)
        self.text_widget.pack(pady=10)
        self.text_widget.insert(tk.END, "What would you like to do?")

        # Create a button to open the write window
        open_write_button = tk.Button(root, text="Add books", command=self.open_add_window)
        open_write_button.pack(pady=0)
        # Create a button to open the remove window
        open_remove_button = tk.Button(root, text="Remove books", command=self.open_books_window) #open remove window
        open_remove_button.pack(pady=0)
        # Create a button to open the books window
        open_books_button = tk.Button(root, text="Show all books", command=self.open_books_window)
        open_books_button.pack(pady=0)

    def open_books_window(self):
        database_info()
        my_model = Model()
        my_view = view(my_model)
        rows_books = my_model.get_rows()
        books_window = tk.Toplevel(self.root)
        app_books = BookWindow(books_window, num_books=rows_books)

    def open_add_window(self):
        database_info()
        add_window = tk.Toplevel(self.root)
        app_add = AddWindow(add_window)


if __name__ == "__main__":
    root = tk.Tk()
    app_main = MainWindow(root)
    root.mainloop()