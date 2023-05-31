class Company:
    global levels
    levels = {1: 'junior', 2: 'middle', 3: 'senior', 4: 'lead'}
    def __init__(self, index):
        self._index = index
        self.level = levels[index]
    def _level_up(self):
        if self._index < 4:
            self._index += 1
            self.level = levels[self._index+1]
        else:
            pass
    def is_lead(self):
        if self._index == 4:
            print('This person is a lead')
        else:
            print("This person isn't a lead ")
class Programmer(Company):
    def __init__(self, name, age):
        super().__init__(1)
        self.name = name
        self.age = age
    def work(self):
        if self._index != 4:
            print('This person has worked long enough to get a promotion.')
            self._level_up()
            print(f'Now this programmer is a {levels[self._index]}')
        else:
            print('This programmer is a lead already')
    def info(self):
        print(f'Name:{self.name}, Age:{self.age}, level:{self.level}')
    @staticmethod
    def knowledge_base():
        print('If you want to write python code, you better use pycharm')

Programmer.knowledge_base()
Overone = Company(3)
prog1 = Programmer('Stanislav', '17')
prog1.work()
prog1.work()
prog1.work()
prog1.is_lead()




