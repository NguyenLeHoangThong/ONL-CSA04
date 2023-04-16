import sqlite3
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'test.db')  
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS student
                  (id INT PRIMARY KEY, name TEXT, age INTEGER)''')

cursor.execute('''
               INSERT INTO test (
                     id,
                     testName
                 )
                 VALUES (
                     5,
                     'thong'
                 );
               ''')

cursor.execute('SELECT * FROM test')
rows = cursor.fetchall()
print(rows)

