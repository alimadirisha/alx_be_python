class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
        
    def deposit_amount(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: {self.account_balance:.2f}")
        else:
            print("Deposit amount must be positive")
        
    def withdraw_amount(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds")
            return False
        elif amount <= 0:
            Print("Withdrawal amount must be positive")
            return False
        else:
            self.account_balance -= amount
            print(f"Withdrew: ${self.account_balance:.2f}")
                
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}:2f")   
    
account1 = BankAccount()

# Deposit money
account1.deposit_amount(100)    

#Withdraw money
account1.withdraw_amount(50)

# Check balance
account1.display_balance()         