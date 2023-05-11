import sys

def calculator(a, b):
    def operation(c):
        def ex():
            sys.exit(0)
        def div():
            try:
                return f'The  result of division is {a / b}'
            except ZeroDivisionError:
                return "You can't divide by zero!"
        def mult():
            return f'The result of multiplication is {a * b}'
        def sm():
            return f'The result of summation is {a + b}'
        def subtr():
            return f'The result of subtraction is {a - b}'
        def idk():
            return 'unknown operation'
        if c == '0':
            print(ex())
        elif c == '/':
            print(div())
        elif c == '*':
            print(mult())
        elif c == '+':
            print(sm())
        elif c == '-':
            print(subtr())
        else:
            print('Unknown operation!')
        return ''
    return operation(input('Enter an operation(0 to exit, /, *, +, -): '))
while True:
    try:
        print(calculator(int(input('Enter the first number: ')), int(input('Enter the second number: '))))
    except ValueError:
        print("These aren't numbers!")