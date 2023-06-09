import sqlite3
#1
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS mytable
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, col_2 TEXT, col_3 TEXT)''')
cursor.execute("INSERT INTO mytable (col_2, col_3) VALUES ('hello', '!')")
cursor.execute("INSERT INTO mytable (col_2) VALUES ('world')")
cursor.execute("DELETE FROM mytable WHERE col_3")
cursor.execute("UPDATE mytable SET col_2=? WHERE id=2", ('hello world',))
with open('data.txt', 'w') as file:
    cursor.execute("SELECT * FROM mytable")
    k = cursor.fetchall()
    for i in k:
        file.write(str(i[0]) + '\t' + str(i[1]) + '\t' + str(i[2]) + '\n')

#2
cursor.execute("SELECT COUNT(*) FROM mytable")
count = cursor.fetchone()[0]
half_count = count // 2
cursor.execute(f"DELETE FROM mytable WHERE id <= {half_count}")
cursor.execute("UPDATE mytable SET col_2=?, col_3=?", ('hello', 'world'))
conn.commit()
conn.close()

#3
conn = sqlite3.connect('my_db.db')
cursor = conn.cursor()
cursor.execute('''create table if not exists str_table(id integer primary key autoincrement, col_1 text)''')
cursor.execute('''create table if not exists int_table(id integer primary key autoincrement, col_1 integer)''')
my_list = ['Home', 'Work', 29, 9, 2022]
for i in my_list:
    if isinstance(i, int):
        if i % 2 == 0:
            cursor.execute(f'''insert into int_table(col_1) values({i})''')
        else:
            cursor.execute(f'''insert into str_table(col_1) values('нечётное')''')
        pass
    elif isinstance(i, str):
        cursor.execute(f'''insert into str_table(col_1) values(?)''', ({str(i)}))
        cursor.execute(f'''insert into int_table(col_1) values(?)''', (str({len(i)})))
k = cursor.fetchall()
if sum(k) > 5:
    cursor.execute('''delete from str_table where id=1''')
else:
    cursor.execute('''update str_table set col_1 = 'hello' where id = 1''')
conn.commit()
conn.close()