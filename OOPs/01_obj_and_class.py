print("Hello MFs")


class BankAccount :
    def __init__(self , name , balance) :
        self.acc_holder_name = name
        self.balance = balance;
    
    def deposit_money(self , money_added) :
        self.balance += money_added

    def withdraw_money(self , money_taken) :
        self.balance -= money_taken

    def check_balance(self) :
        return f"MY Account Balance :{self.balance}" 


bank1 = BankAccount("Jay", 400000000)
print(bank1.check_balance())
print("\nAfter depositing 100 00 00 000:")
bank1.deposit_money(1000000000);
print(bank1.check_balance())
print("\nAfter withdrawing 10 00 00 000:")
bank1.withdraw_money(100000000);
print(bank1.check_balance())

