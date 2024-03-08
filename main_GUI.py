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
        root.resizable(False, False)
        window_height = 160
        window_width = 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        my_model = Model()
        my_view = view(my_model)
        self.num_books = num_books

        scrollbar = tk.Scrollbar(root)
        scrollbar.pack( side = 'right', fill='y' )

        mylist = tk.Listbox(root, yscrollcommand = scrollbar.set )
        for i in range(self.num_books):
            ##mylist.insert('end', "This is line number " + str(line))
            book_id = str(my_model.get_row(i, 'id')).replace('(','').replace(')','').replace(',','')
            book_title = str(my_model.get_row(i, 'title')).replace('(','').replace(')','').replace(',','')
            book_author = str(my_model.get_row(i, 'author')).replace('(','').replace(')','').replace(',','')
            book_genre = str(my_model.get_row(i, 'genre')).replace('(','').replace(')','').replace(',','')
            book_year = str(my_model.get_row(i, 'publication_year')).replace('(','').replace(')','').replace(',','')
            mylist.insert('end', (str(i+1)+'.          ID: '+book_id+',     Title: '+book_title+',     Author: '+book_author+',     Genre: '+book_genre+',     Year: '+book_year))
        
        mylist.pack( fill = 'both' )
        scrollbar.config( command = mylist.yview )

class AddWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Add books")
        root.resizable(False, False)
        window_height = 325
        window_width = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        book_label = tk.Label(root, text='Book name:')
        book_label.pack()
        self.book_entry = tk.Entry(root)
        self.book_entry.pack(pady=10)
        author_label = tk.Label(root, text='Book author:')
        author_label.pack()
        self.author_entry = tk.Entry(root)
        self.author_entry.pack(pady=10)
        genre_label = tk.Label(root, text='Book genre:')
        genre_label.pack()
        self.genre_entry = tk.Entry(root)
        self.genre_entry.pack(pady=10)
        year_label = tk.Label(root, text='Year published:')
        year_label.pack()
        self.year_entry = tk.Entry(root)
        self.year_entry.pack(pady=10)
        add_button = tk.Button(root, text="Add book", command=self.add_books)
        add_button.pack(pady=10)
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def add_books(self):
        my_model = Model()
        my_view = view(my_model)
        addbook = self.book_entry.get()
        addauthor = self.author_entry.get()
        addgenre = self.genre_entry.get()
        addyear = self.year_entry.get()
        if(addbook != "" and addauthor != "" and addgenre != "" and addyear != ""):
            my_model.add_data(addbook, addauthor, addgenre, addyear)
            self.book_entry.delete(0, 'end')
            self.author_entry.delete(0, 'end')
            self.genre_entry.delete(0, 'end')
            self.year_entry.delete(0, 'end')
            result_message = 'Successfully added book "' + addbook +'".'
            self.result_label.config(text=result_message)
        else:
            result_message = 'Book not added: One or more fields left empty.'
            self.result_label.config(text=result_message)

class RemoveWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Remove books")
        root.resizable(False, False)
        window_height = 150
        window_width = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        id_label = tk.Label(root, text='Book ID:')
        id_label.pack()
        self.id_entry = tk.Entry(root)
        self.id_entry.pack(pady=10)

        remove_button = tk.Button(root, text="Remove book", command=self.remove_books)
        remove_button.pack(pady=10)
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def remove_books(self):
        my_model = Model()
        my_view = view(my_model)
        removebook = str(self.id_entry.get())
        if(removebook != ""):
            try:
                removedtitle = str(my_model.get_row_id(removebook, 'title')).replace('(','').replace(')','').replace(',','')
                my_model.remove_data(removebook)
                self.id_entry.delete(0, 'end')
                result_message = 'Successfully removed book ' + removedtitle +'.'
                self.result_label.config(text=result_message)
            except IndexError:
                result_message = 'Book not removed: Book with ID of "'+removebook+'" does not exist.'
                self.result_label.config(text=result_message)
        else:
            result_message = 'Book not removed: Field cannot be empty.'
            self.result_label.config(text=result_message)

class BorrowWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Borrow a Book")
        root.resizable(False, False)
        window_height = 150
        window_width = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        
        book_label = tk.Label(root, text='Enter patron name and book title')
        book_label.pack(pady=10)

        self.patron_entry = tk.Entry(root)
        self.patron_entry.pack(pady=5)

        self.book_entry = tk.Entry(root)
        self.book_entry.pack(pady=5)

        borrow_button = tk.Button(root, text="Borrow", command=self.borrow_book)
        borrow_button.pack(pady=10)

    def borrow_book(self):
        patron_name = self.patron_entry.get()
        book_title = self.book_entry.get()

        # Call the library function to borrow the book
        library = Library('books.db')
        library.borrow_book(patron_name, book_title)

        self.patron_entry.delete(0, 'end')
        self.book_entry.delete(0, 'end')

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Main")
        root.resizable(False, False)
        window_height = 150
        window_width = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        
        book_label = tk.Label(root, text='What would you like to do?')
        book_label.pack(pady=10)

        # Create a button to open the write window
        open_write_button = tk.Button(root, text="Add books", command=self.open_add_window)
        open_write_button.pack(pady=0)
        # Create a button to open the remove window
        open_remove_button = tk.Button(root, text="Remove books", command=self.open_remove_window)
        open_remove_button.pack(pady=0)
        # Create a button to open the books window
        open_books_button = tk.Button(root, text="Show all books", command=self.open_books_window)
        open_books_button.pack(pady=0)
        # Create a button to open the borrow window
        open_borrow_button = tk.Button(root, text="Borrow a book", command=self.open_borrow_window)
        open_borrow_button.pack(pady=0)

    def open_books_window(self):
        my_model = Model()
        my_view = view(my_model)
        rows_books = my_model.get_rows()
        books_window = tk.Toplevel(self.root)
        app_books = BookWindow(books_window, num_books=rows_books)

    def open_add_window(self):
        add_window = tk.Toplevel(self.root)
        app_add = AddWindow(add_window)

    def open_remove_window(self):
        remove_window = tk.Toplevel(self.root)
        app_add = RemoveWindow(remove_window)

    def open_borrow_window(self):
        borrow_window = tk.Toplevel(self.root)
        app_borrow = BorrowWindow(borrow_window)


if __name__ == "__main__":
    database_info()
    root = tk.Tk()
    app_main = MainWindow(root)
    root.mainloop()
