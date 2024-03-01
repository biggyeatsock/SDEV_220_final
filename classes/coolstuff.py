class Model:
    def __init__(self):
        import sqlite3
        self.conn = sqlite3.connect('books.db')
        self.cursor = self.conn.cursor()
    
    def get_data(self):
        self.cursor.execute('SELECT * FROM books')
        return self.cursor.fetchall()
    
    def add_data(self, title, author, genre, publication_year): # Adds a new book into the database
        self.cursor.execute('INSERT INTO books (title, author, genre, publication_year) VALUES (?, ?, ?, ?)', (title, author, genre, publication_year))# Takes a new book and imputs it into the database.
        self.conn.commit()
    
    def remove_data(self, id): # Removes book from the database file. 
        self.cursor.execute('DELETE FROM books WHERE id=?', (id,)) # Takes the given ID and uses it to remove said book from databse.
        self.conn.commit()

    def get_rows(self):
        self.cursor.execute('SELECT * FROM books')
        results = self.cursor.fetchall()
        return len(results)
    
    def get_row(self, id):
        self.cursor.execute('SELECT title FROM books')
        results = self.cursor.fetchall()
        return results[id]

class view:
    def __init__(self, model):
        self.model = model
        
    def show_data(self):
        data = self.model.get_data()
        for row in data:
            print(f'\n{row}')









