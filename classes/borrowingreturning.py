import sqlite3

from datetime import datetime, timedelta

def borrow_time():
    current_date = datetime.now()
    future_date = current_date + timedelta(days=14)
    formatted_date = future_date.strftime("%B %d")
    suffix = "th" if 11 <= future_date.day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(future_date.day % 10, "th")
    formatted_date += suffix
    return formatted_date

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file

    def create_connection(self):
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except sqlite3.Error as e:
            print("Error connecting to the database:", e)
            return None

    def execute_query(self, query, params=None):
        try:
            conn = self.create_connection()
            if conn:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                conn.commit()
                conn.close()
        except sqlite3.Error as e:
            print("Error executing query:", e)
    
    def fetch_data(self, query, params=None):
        try:
            conn = self.create_connection()
            if conn:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                data = cursor.fetchall()
                conn.close()
                return data
        except sqlite3.Error as e:
            print("Error fetching data:", e)
    
    def remove_book(self, book_title):
        """Remove a book from the database."""
        query = "DELETE FROM books WHERE title = ?"
        self.execute_query(query, (book_title,))

    def add_book(self, book):
        """Add a book to the database."""
        query = "INSERT INTO books (title, author) VALUES (?, ?)"
        self.execute_query(query, (book["title"], book["author"]))

    def update_borrow_name(self, book_id, borrow_name):
        """Update the borrow_name for a book."""
        try:
            conn = self.create_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE books
                    SET borrow_name = ?
                    WHERE id = ?
                ''', (borrow_name, book_id))
                conn.commit()
                conn.close()
        except sqlite3.Error as e:
            print("Error updating borrow name:", e)


if __name__ == "__main__":
    db_manager = DatabaseManager('books.db')
