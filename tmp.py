# This just a test file.
# This tests to see if a database file has been created, and if it is, it prints the size of the file.

import sqlite3
from os.path import isfile, getsize
# conn = sqlite3.connect('database.db')
try: 
    if not isfile('database.db'):
        raise sqlite3.OperationalError
    
    if isfile('database.db'):
        print(f'\nDatabase file size: {getsize("books.db")} bytes')

except sqlite3.OperationalError as e:
    print(f'File Not found')
