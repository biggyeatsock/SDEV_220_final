class Model:
    def __init__(self):
        import sqlite3
        self.conn = sqlite3.connect('books.db')
        self.cursor = self.conn.cursor()
    
    def get_data(self):
        self.cursor.execute('SELECT * FROM books')
        return self.cursor.fetchall()

class view:
    def __init__(self, model):
        self.model = model
        
    def show_data(self):
        data = self.model.get_data()
        for row in data:
            print(f'\n{row}')





