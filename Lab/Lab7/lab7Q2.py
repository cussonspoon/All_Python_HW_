#Question 2
class BankAccount:
    def __init__(self, bankname = "K+", ownername = "Spoon", accountnum = "0893697896", currentbalance = 0.0):
        self.bankname = bankname
        self.ownername = ownername
        self.accountnum = accountnum
        self.currentbalance = currentbalance
    def deposit(self, n):
        if n >= 0:
            self.currentbalance += n
            return self.currentbalance
        else:
            print("The deposited value cannot be negative")
    def withdraw(self, n):
        if n >= 0:
            if self.currentbalance - n >= 0.0:
                self.currentbalance -= n
                return self.currentbalance
            else:
                self.currentbalance = "Exceed amount of current balance"
                return self.currentbalance
        else:
            print("The withdraw value cannot be negative")
    def printit(self):
        print("Current balance : " + str(self.currentbalance))
bank1 = BankAccount()
bank1.deposit(45.5)
bank1.printit()
bank1.withdraw(20)
bank1.printit()
bank1.withdraw(99999999)
bank1.printit()
bank1.deposit(-15)
bank1.withdraw(-15)

