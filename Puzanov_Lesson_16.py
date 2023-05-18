l = [1, 2, 3, 4, 5, 6]
def modify_list(m):
    i = 0
    while i<len(l):
        if m[i] % 2 == 0:
            m[i] //= 2
            i += 1
        else:
            m.pop(i)
modify_list(l)
print(l)