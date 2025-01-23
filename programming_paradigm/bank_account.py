class BankAccount:
    def __init__(self, account_balance=0,):
        self.account_balance = account_balance
        
    def deposit(self, amount):
        self.account_balance += amount
        print(f" Deposited: ${self.account_balance:.1f} ")
       
        
    def withdraw(self, amount):
        if amount > self.account_balance:
            return True
        else:
            self.account_balance -= amount
                
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")   
    
# account = BankAccount()

# # Deposit cash
# account.deposit(317)

# # Withdraw cash
# account.withdraw(50)
# account.withdraw(350)

# # Check balance
# account.display_balance()         