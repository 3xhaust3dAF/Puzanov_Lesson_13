class BankAccount:
    default_number = '0'
    default_balance = 0

    def __init__(self, number=default_number, balance=default_balance):
        self.__account_number = number
        self.__balance = balance
    def get_account_number(self):
        print(f'Номер аккаунта - {self.__account_number}')
    def get_balance(self):
        print(f'Счёт - {self.__balance}')
    def deposit(self, add):
        self.__balance += add
        print(f'Добавлено на счёт {add} рублей, новый счёт - {self.__balance} рублей')
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f'Снято со счёта {amount} рублей, новый счёт - {self.__balance} рублей')
        else:
            print(f'Недостаточно средств для снятия {amount} рублей со счёта')

user1 = BankAccount('123456789', 1000)
user1.get_balance()
user1.get_account_number()
user1.deposit(500)
user1.withdraw(1500)