class Bank:
    def __init__(self,acc_name,acc_number,balance=0):
        self.acc_name=acc_name
        self.acc_number=acc_number
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"amount {self.balance} is deposited")
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"amount {self.balance} is credited")
        else:
            print(f"you dont have required amount in bank account to withdraw \n your balance is: {self.balance}")
    def acc_balance(self):
        print(f"account holder name: {self.acc_name}  account number {self.acc_number} has the balance of : {self.balance}")
b1=Bank("Deepak",123456,13000.5)
b1.deposit(2000)
b1.acc_balance()