#Puzanov_Lesson_12. Я решил скинуть два в одном: загрузил 12 дз на гитхаб.
#1
while True:
    txt = input('Введите текст. Если хотите завершить, введите пустую строку: ')
    if txt:
        f = open('example.txt', 'a+', encoding='utf-8')
        f.write(f'\n{txt}')
    if not txt:
        break

f.close()

#2 Пусть будет тот же файл
ls = []
with open('example.txt') as m:
    j = m.read()
    ls = j.split('\n')
    ls[0].replace('\n', '')#Всё равно \н считает за строку :(
    print(f'Количество строк - {len(ls)}')
    for i in range(len(ls)):
        print(f'Количество символов в {i+1} строке - {len(ls[i])}')



#3
ll = [1, 2, 3, 4, 5, 'абв', 'абвг','абвгд']
ln = []
lc = []
for i in ll:
    if type(i) == int:
        ln.append(str(i))
    elif type(i) == str:
        lc.append(str(i))
lc.sort(key=len)
ln.sort()
lc.extend(ln)
a = ','.join(lc)
d = open('example1.txt', 'w+', encoding='utf-8')
d.write(a)
d.seek(0)
print(*d)
d.close()

#4
import os
os.chdir('C:/Users/puzan/Desktop')
try:
    os.makedirs('my_name')
except FileExistsError: #при многочисленных тестированиях кода у меня выдавало ошибку про сущ. файла, поэтому я в искл добавил
    print('Файл уже был создан! Продолжаю работу')
os.chdir('C:/Users/puzan/Desktop/my_name')
try:
    for i in range(3):
        g = open(f'test_{str(i+1)}.txt', 'w+')
except:
    print('Такие файлы уже есть! Продолжаю работу')#то же самое
for i in range(3):# - на этом этапе выдаёт ошибку, что нельзя работать с файлом, тк его занимает другой процесс :(
    os.rename(f'test_{str(i+1)}.txt', f'rename_{str(i+1)}.txt')
for i in range(3):
    os.remove(f'C:/Users/puzan/Desktop/my_name/rename_{str(i+1)}.txt')
os.chdir('..')
os.rmdir('my_name')


