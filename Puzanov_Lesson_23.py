import sys

from math import sqrt

from time import sleep

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton




class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.my_input = 0
        self.operand_1 = 0
        self.operand_2 = 0
        self.operation = 0

    def initUI(self):
        self.setGeometry(300, 300, 250, 350)
        self.setWindowTitle('calculator')
        self.setFixedSize(250, 350)

        #Label
        self.label = QLabel(self)
        self.label.resize(325, 50)
        self.label.move(0, 0)
        self.label.setText('Enter values')
        #Buttons-numbers
        self.num_1 = QPushButton('1', self)
        self.num_1.resize(50, 50)
        self.num_1.move(0, 150)

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(50, 50)
        self.num_2.move(50, 150)

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(50, 50)
        self.num_3.move(100, 150)

        self.num_4 = QPushButton('4', self)
        self.num_4.resize(50, 50)
        self.num_4.move(0, 200)

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(50, 50)
        self.num_5.move(50, 200)

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(50, 50)
        self.num_6.move(100, 200)

        self.num_7 = QPushButton('7', self)
        self.num_7.resize(50, 50)
        self.num_7.move(0, 250)

        self.num_8 = QPushButton('8', self)
        self.num_8.resize(50, 50)
        self.num_8.move(50, 250)

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(50, 50)
        self.num_9.move(100, 250)

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(50, 50)
        self.num_0.move(50, 300)

        #Buttons-actions
        self.plus = QPushButton('+', self)
        self.plus.resize(50, 50)
        self.plus.move(150, 150)

        self.minus = QPushButton('-', self)
        self.minus.resize(50, 50)
        self.minus.move(150, 200)

        self.mul = QPushButton('х', self)
        self.mul.resize(50, 50)
        self.mul.move(150, 250)

        self.power = QPushButton('pow_2', self)
        self.power.resize(50, 50)
        self.power.move(200, 250)

        self.sqrt = QPushButton('sqrt', self)
        self.sqrt.resize(50, 50)
        self.sqrt.move(200, 300)

        self.cel = QPushButton('Z', self)
        self.cel.resize(50,50)
        self.cel.move(200, 150)

        self.ost = QPushButton('ost', self)
        self.ost.resize(50, 50)
        self.ost.move(200, 200)

        self.div = QPushButton(':', self)
        self.div.resize(50, 50)
        self.div.move(150, 300)

        self.but_c = QPushButton('c', self)
        self.but_c.resize(50, 50)
        self.but_c.move(0, 300)

        self.but_e = QPushButton('=', self)
        self.but_e.resize(50, 50)
        self.but_e.move(100, 300)
        #Button connection
        self.num_0.clicked.connect(self.n0)
        self.num_1.clicked.connect(self.n1)
        self.num_2.clicked.connect(self.n2)
        self.num_3.clicked.connect(self.n3)
        self.num_4.clicked.connect(self.n4)
        self.num_5.clicked.connect(self.n5)
        self.num_6.clicked.connect(self.n6)
        self.num_7.clicked.connect(self.n7)
        self.num_8.clicked.connect(self.n8)
        self.num_9.clicked.connect(self.n9)
        self.plus.clicked.connect(self.pl)
        self.minus.clicked.connect(self.mn)
        self.mul.clicked.connect(self.umn)
        self.div.clicked.connect(self.rzd)
        self.but_c.clicked.connect(self.clean)
        self.but_e.clicked.connect(self.ravno)
        self.ost.clicked.connect(self.ost_f)
        self.power.clicked.connect(self.pow_f)
        self.sqrt.clicked.connect(self.sqrt_f)
        self.cel.clicked.connect(self.z_f)


    #Button fuctions
    def enter_value(self):
        if self.label.text() == 'Enter values':
            self.label.setText('')
        self.label.setText(self.label.text() + self.my_input)
    def n1(self):
        self.my_input = '1'
        self.enter_value()
    def n2(self):
        self.my_input = '2'
        self.enter_value()
    def n3(self):
        self.my_input = '3'
        self.enter_value()
    def n4(self):
        self.my_input = '4'
        self.enter_value()
    def n5(self):
        self.my_input = '5'
        self.enter_value()
    def n6(self):
        self.my_input = '6'
        self.enter_value()
    def n7(self):
        self.my_input = '7'
        self.enter_value()
    def n8(self):
        self.my_input = '8'
        self.enter_value()
    def n9(self):
        self.my_input = '9'
        self.enter_value()
    def n0(self):
        self.my_input = '0'
        self.enter_value()
    def pl(self):
        self.operation = '+'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def pow_f(self):
        self.operation = '**'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def sqrt_f(self):
        self.operation = 'sqrt'
        self.operand_1 = float(self.label.text())
        self.label.setText(f'sqrt({self.label.text()})')

    def z_f(self):
        self.operation = '//'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def ost_f(self):
        self.operation = 'ostatok'
        self.operand_1 = float(self.label.text())
        self.label.setText('')


    def mn(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def umn(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def rzd(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def clean(self):
        self.label.setText('')

    def ravno(self):
        if self.operation != 'sqrt':
            self.operand_2 = float(self.label.text())
        if self.operation == '+': self.label.setText(str(self.operand_1 + self.operand_2))
        elif self.operation == '*': self.label.setText(str(self.operand_1 * self.operand_2))
        elif self.operation == '/':
            try:
                self.operand_1 / self.operand_2
            except BaseException:
                self.label.setText('Division by zero!')
                sleep(1)
                self.label.setText('')
            else:
                self.label.setText(str(self.operand_1 / self.operand_2))
        elif self.operation == '-':
            self.label.setText(str(self.operand_1 - self.operand_2))
        elif self.operation == '**': self.label.setText(str(self.operand_1 ** self.operand_2))
        elif self.operation == 'sqrt':
            if self.operand_1 < 0:
                self.label.setText("Can't take square root of negative number!")
                sleep(1)
                self.label.setText('')
            else:
                self.label.setText(str(sqrt(self.operand_1)))
        elif self.operation == '//': self.label.setText(str(self.operand_1 // self.operand_2))
        elif self.operation == 'ostatok': self.label.setText(str(self.operand_1 % self.operand_2))

app = QApplication(sys.argv)

my_calculator = Calculator()
my_calculator.show()
sys.exit(app.exec())
