class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.holder = account_holder
        self.balance = initial_balance

    def transfer_funds(self, other_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print("transfer confirmed")
        else:
            print("error : insufficient bank balance")

    def __str__(self):
        print(f"account_holder : {self.holder}\nbalance : {self.balance}")
        


