class BankAccount:
    def __init__(self, account_balance=0,):
        self.account_balance = account_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        
    def withdraw(self, amount):
        if amount > self.account_balance:                                                                          
            return False
        elif amount <= 0:
            return False
        else:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")
                
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