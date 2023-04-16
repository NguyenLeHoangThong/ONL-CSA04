# pgAmin 4
# phpAdmin (XAMPP)

import sqlite3
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'truongHoc.db')

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute('''          
               CREATE TABLE IF NOT EXISTS HocSinh (
                    ID int,
                    TEN varchar(255),
                    DIEM_TRUNG_BINH double,
                    PRIMARY KEY (ID)
                );
               ''')

cursor.execute('''          
               CREATE TABLE IF NOT EXISTS LopHoc (
                    ID int,
                    TEN_LOP varchar(255),
                    PRIMARY KEY (ID)
                );
               ''')


cursor.execute('''          
               INSERT INTO HocSinh (ID, TEN, DIEM_TRUNG_BINH)
                VALUES (2, 'Vuong Ton', 9.5);
               ''')

cursor.execute('''          
               SELECT *
                FROM HocSinh;
               ''')

print(cursor.fetchall())


conn.close()
