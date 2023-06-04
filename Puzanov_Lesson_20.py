#Уже есть созданная в access БД
import sqlite3
conn = sqlite3.connect('data.sqlite')
cursor = conn.cursor()
cursor.execute('''SELECT * FROM Таблица1''')
print(*cursor)#вывод всей таблицы
cursor.execute('''SELECT task FROM Таблица1 WHERE status = 'done' ''')
print(*cursor)#Выводит задания, которые уже выполнены
cursor.execute('''SELECT * FROM Таблица1 WHERE description LIKE '%lead%' ''')
print(*cursor)#выводит задачу со всеми свойствами, которой занимается лид
cursor.execute('''SELECT * FROM Таблица1 ORDER BY status''')
print(*cursor)#сортировка задач по мере их выполнения