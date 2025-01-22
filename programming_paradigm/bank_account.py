class BankAccount:
    def __init__(self, initial_balance=0,):
        self.account_balance = initial_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${self.account_balance:.1f}")
        else:
            print("Deposit amount must be positive")
        
    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds")
            return False
        elif amount <= 0:
            Print("Withdrawal amount must be positive")
            return False
        else:
            self.account_balance -= amount
            print(f"Withdrew: ${self.account_balance:.1f}")
                
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")   
    
account = BankAccount()

# Deposit money
account.deposit(67)    

#Withdraw money
account.withdraw(20)

# Check balance
account.display_balance()         