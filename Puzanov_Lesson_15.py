#1
def f_info(var):
    nms = 0
    chs = 0
    lngth = 0
    odd = 0
    chs_1 = 0
    if type(var) == tuple:
        for i in var:
            if str(i).isdigit():
                continue
            elif str(i).isalpha():
                lngth += len(i)
        return f' {lngth} символа(ов)'
    elif type(var) == list:
        for i in var:
            for j in var[str(i).index(var)]:
                if str(j).isdigit():
                    nms += 1
                elif str(j).isalpha():
                    chs += 1
        return f'{nms} числа, {chs} буквы'
    elif type(var) == int:
        for o in var:
            if o % 2 != 0:
                odd += 1
        return f'{odd} нечётных цифр'
    elif type(var) == str:
        for p in var:
            if str(p).isalpha():
                chs_1 += 1
        return f'{chs_1} - кол-во букв'
    else:
        raise TypeError('Такой тип не поддерживается')

f_info('123asd')

