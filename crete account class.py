# Create account class with 2 attribute - balance & account no
# Create methods for debit ,credit & printing the balance

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    # debit method
    def debit(self,ammount):
        self.balance-=ammount
        print("Rs.",ammount,"was debited")
    #credit method 
    def credit(self,ammount):
        self.balance+=ammount 
        print("Rs.",ammount,"was credited")
    def balance_val(self):
        return self.balance    

s1= Account(1000,2503111640018)   
s1.debit(99)
print(s1.balance_val())

# or 
class Account:
    def __init__(self,bal,acc):
        self.balance= bal
        self.account_n0 = acc
    # debit method
    def debit(self,ammount):
        self.balance-=ammount
        print("Rs.",ammount,"was debited")
        print("Total blance=",self.balance)
    #credit method
    def credit(self,ammount):
        self.balance+=ammount
        print("Rs.",ammount,"Was credited")
        print("Total blance=",self.balance)
    # total balance
    def get_balance(self):
        return self.balance

acc1 = Account(1000,2503111640019)
acc1.debit(232)
acc1.credit(2000)

