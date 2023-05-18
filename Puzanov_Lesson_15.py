#1
s = [1, 2, 3, 'a', 'bc8?']
def f_info(var):
    nms = 0
    chs = 0
    lngth = 0
    odd = 0
    chs_1 = 0
    if isinstance(var, tuple):
        for i in var:
            lngth += len(i)
        print(f' {lngth} - длина всех строк')
    elif isinstance(var, list):
        for i in var:
            if isinstance(i, str):
                for j in i:
                    if str(j).isdigit():
                        nms += 1
                    elif str(j).isalpha():
                        chs += 1
            else:
                if str(i).isdigit():
                    nms += 1
                elif str(i).isalpha():
                    chs += 1
        print(f'{nms} числа, {chs} буквы')
    elif isinstance(var, int):
        for o in range(var):
            if o % 2 != 0:
                odd += 1
        print(f'{odd} нечётных цифр')
    elif isinstance(var, str):
        for p in var:
            if str(p).isalpha():
                chs_1 += 1
        print(f'{chs_1} - кол-во букв')
    else:
        raise TypeError('Такой тип не поддерживается')
#2
def print_data_type(fx):
    print(f'Тип данныx - {type(s).__name__}')
    def wrapper(args):
        a = []
        fx(args)
        try:
            for i in args:
                if isinstance(i, int):
                    if 'int' not in a:
                        a.append('int')
                if isinstance(i, str):
                    if 'str' not in a:
                        a.append('str')
            print(f'{a} - типы встречающихся данных')
        except TypeError:
            if 'int' not in a:
                a.append('int')
            print(f'{a} - типы встречающихся данных')
    return wrapper

@print_data_type
def data(m):
    print(f'Обработка: {m}')
data([1, 2, 3, 'a', 'bc8?'])



f_info([1, 2, 3, 'a', 'bc8?'])

#2

