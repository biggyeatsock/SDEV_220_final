import sqlite3

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file

    def create_connection(self):
        return sqlite3.connect(self.db_file)

    def execute_query(self, query, params=None):
        conn = self.create_connection()
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        conn.close()

    def fetch_data(self, query, params=None):
        conn = self.create_connection()
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data

# Define Library class
class Library:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def search_books(self, keyword):
        """Search for books by title or author."""
        try:
            conn = self.db_manager.create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM books
                WHERE title LIKE ? OR author LIKE ?
            ''', ('%' + keyword + '%', '%' + keyword + '%'))
            books = cursor.fetchall()
            conn.close()

            if books:
                print("Search results:")
                for book in books:
                    print(Book(*book))
            else:
                print("No books found matching the search criteria.")
        except sqlite3.Error as e:
            print("Error searching books:", e)

    def borrow_book(self, patron, book_title):
        """Allow a patron to borrow a book."""
        try:
            conn = self.db_manager.create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM books
                WHERE title = ?
            ''', (book_title,))
            book = cursor.fetchone()
            conn.close()

            if book:
                borrowed_book = Book(*book)
                patron.borrow_book(borrowed_book)
                self.db_manager.remove_book(book_title)
            else:
                print(f"The book '{book_title}' is not available.")
        except sqlite3.Error as e:
            print("Error borrowing book:", e)

    def return_book(self, patron, book_title):
        """Allow a patron to return a book."""
        try:
            returned_book = None
            conn = self.db_manager.create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM books
                WHERE title = ?
            ''', (book_title,))
            book = cursor.fetchone()
            conn.close()

            if book:
                returned_book = Book(*book)
                patron.return_book(returned_book)
                self.db_manager.add_book(returned_book)
            else:
                print(f"The book '{book_title}' is not valid.")
        except sqlite3.Error as e:
            print("Error returning book:", e)

# Books.db file
db_manager = DatabaseManager('books.db')

library = Library(db_manager)
