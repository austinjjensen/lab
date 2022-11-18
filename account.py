class Account:
    def __init__(self, name):
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount):
        if(amount >= 0 ):
            self.account_balance = self.account_balance + amount
        else:
            print('Cannot deposit a negative amount')

    def withdraw(self, amount):
        if(amount <= self.account_balance):
            self.account_balance = self.account_balance - amount
        else:
            print('Cannot withdraw more than your account balance')

    def get_name(self):
        print('Name: ', self.account_name)

    def get_balance(self):
        print('Account Balance: ', self.account_balance)
