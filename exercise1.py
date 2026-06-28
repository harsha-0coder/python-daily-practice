# ATM system 
# assume that, owner has 10,000 amount as default

class BankAccount:
    def __init__(self, name, acc_num, balance = 10000):
        self.owner = name
        self.account = acc_num
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("invalid amount")
            # return
        else:
            self.balance += amount
            print(f"your Bank account has credited {amount}")
        
        
    def withdraw(self, amount):
        if self.balance < amount:
            print("insufficient Balance")
        else:
            self.balance -= amount
            print(f"your Bank account has debited {amount}")

    def check_balance(self):
        print(f"the total amount in your bank account has {self.balance}")

person1 = BankAccount("Harsh", 12345678)
person1.deposit(-1000)
# person1.deposit(5000)
# person1.withdraw(12000)
# person1.withdraw(5000)
# person1.check_balance()   