import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """Create a table to store books."""
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS books
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        genre TEXT NOT NULL,
        publication_year INTEGER NOT NULL,
        borrow_date TEXT,
        borrow_name TEXT,
        return_date TEXT)''')
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def insert_book(conn, title, author, genre, publication_year, borrow_name=None, borrow_date=None, return_date=None):
    """Insert a book into the database."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO books (title, author, genre, publication_year, borrow_name, borrow_date, return_date)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, author, genre, publication_year, borrow_name, borrow_date, return_date))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def main():
    database = "books.db"
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        insert_book(conn, "To Kill a Mockingbird", "Harper Lee", "Fiction", 1960)
        insert_book(conn, "1984", "George Orwell", "Dystopian", 1949)
        insert_book(conn, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925)
        insert_book(conn, "Frankenstein", "Mary Shelly", "sci-fi", 1818)
        insert_book(conn, "Animal Farm", "George Orwell", " Allegory", 1945)
        insert_book(conn, "of mice and men", "Jane Austen", "realistic fiction", 1937)
        insert_book(conn, "Pride and Prejudice", "John Steinbeck", "Romance", 1813)
        insert_book(conn, "The war of the worlds", "H.G. Wells", "sci-fi", 1898)
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
