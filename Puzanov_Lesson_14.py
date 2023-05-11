import sys
while True:
    def calculator(a, b):
        def operation(c):
            if c == '0':
                def ex():
                     sys.exit(0)
                ex()
            elif c == '/':
                def div():
                    try:
                        return f'The  result of division is {a / b}'
                    except ZeroDivisionError:
                        return "You can't divide by zero!"
                print(div())
            elif c == '*':
                def mult():
                    return f'The result of multiplication is {a * b}'
                print(mult())
            elif c == '+':
                def sm():
                    return f'The result of summation is {a + b}'
                print(sm())
            elif c == '-':
                def subtr():
                    return f'The result of subtraction is {a - b}'
                print(subtr())
            else:
                def idk():
                    return 'unknown operation'
                print(idk())
            return ''
        print(operation(input('Enter an operation(0 to exit the calculator, /, *, +, -): ')))
        return ''
    try:
        print(calculator(int(input('Enter the first number: ')), int(input('Enter the second number: '))))
    except ValueError:
        print("These aren't numbers!")
