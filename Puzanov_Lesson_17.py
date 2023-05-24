class evaluation:
    def maths(self):
        def summ():
            a = 0
            for o in str(self):
                a += 1
            return a
        summ()
        if isinstance(self, str):
            vowels = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё']
            v_c = []
            c_c = []
            for i in self:
                if i not in vowels:
                    c_c.append(i)
                else:
                    v_c.append(i)
            if len([p for p in v_c]) * len([q for q in c_c]) <= summ():
                print(c_c)
            else:
                print(v_c)

        if isinstance(self, int):
            even = []
            for i in str(self):
                if int(i) % 2 == 0:
                    even.append(int(i))
            s = 0
            for i in even:
                s += i
            print(s * summ())
object = evaluation
object.maths('абвгдеёжз')
#Работает только с русским языком


