class BankAccount:
    def __init__(self, owner):
        self.__owner = owner
        self.__balance = 0
    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
    def withdraw(self, amt):
        if 0 < amt <= self.__balance:
            self.__balance -= amt
    def get_balance(self):
        return self.__balance


def main():
    accountant = BankAccount("Dana")
    accountant.deposit(int(input("Enter amount for deposit: ")))
    print(accountant.get_balance(),"zimbabwean dollars has been deposited")
    accountant.withdraw(int(input("Enter amount for withdraw: ")))
    print(accountant.get_balance(),"zimbabwean dollars has been withdrawn")

main()