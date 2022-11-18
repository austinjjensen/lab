class Account:
    def __init__(self, name):
        """Set default values for account objects"""
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount: float) -> float:
        if(amount >= 0 ):
            self.account_balance = self.account_balance + amount
        else:
            print('Cannot deposit a negative amount')

    def withdraw(self, amount: float) -> float:
        if(amount <= self.account_balance):
            self.account_balance = self.account_balance - amount
        else:
            print('Cannot withdraw more than your account balance')

    def get_name(self: str) -> str:
        print('Name: ', self.account_name)

    def get_balance(self: float) -> float:
        print('Account Balance: ', self.account_balance)
