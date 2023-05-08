import os
#1
while True:
    txt = input('Введите текст. Если хотите завершить, введите пустую строку')
    if not txt:
        break
    f = open('example.txt', 'a+', encoding='utf-8')
    f.write(f'\n{txt}')
f = open('example.txt', 'a+', encoding='utf-8')
f.seek(0)
print(f.readlines())
f.close()

#2 Пусть будет тот же файл
ls = []
with open('example.txt') as m:
    j = m.read()
    ls = j.split('\n')
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
#for i in range((len(ln)-1)):
    #ln[i-1] = str(ln[i-1])
lc.extend(ln)
a = ','.join(lc)
d = open('example1.txt', 'w+', encoding='utf-8')
d.write(a)
d.seek(0)
print(*d)
d.close()

#4
os.chdir('..')
os.chdir('..')
os.open('C:/Users/puzan/Desktop', )
for i in range(3):
    g = open(f'C:/Users/puzan/Desktop/my_name/test_{str(i)}.txt', 'w+')
for i in range(3):
    os.rename(f'test_{str(i)}.txt')
os.rmdir('my_name')


