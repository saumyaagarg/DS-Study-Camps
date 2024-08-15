# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

class Customer:
    def __init__(self, name, acc_no, bal = 0.0):
        self.name = name
        self.acc_no = acc_no
        self.bal = bal

    def deposit(self, amnt):
        if amnt > 0:
            self.bal += amnt
            print(f"Deposit successful! New balance: Rs.{self.bal:.2f}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amnt):
        if 0 < amnt <= self.bal:
            self.bal -= amnt
            print(f"Withdrawal successful! New balance: Rs.{self.bal:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount!")

    def get_balance(self):
        return self.bal

    def __str__(self):
        return f"Customer: {self.name}, Account Number: {self.acc_no}, Balance: Rs.{self.bal:.2f}"

class Bank:
    def __init__(self):
        self.customers = {}

    def add_customer(self, name, acc_no):
        if acc_no in self.customers:
            print("Account number already exists!")
        else:
            self.customers[acc_no] = Customer(name, acc_no)
            print(f"Customer '{name}' added successfully!")

    def remove_customer(self, acc_no):
        if acc_no in self.customers:
            del self.customers[acc_no]
            print(f"Customer with account number {acc_no} removed successfully!")
        else:
            print("Account number not found!")

    def perform_deposit(self, acc_no, amnt):
        if acc_no in self.customers:
            self.customers[acc_no].deposit(amnt)
        else:
            print("Account number not found!")

    def perform_withdrawal(self, acc_no, amnt):
        if acc_no in self.customers:
            self.customers[acc_no].withdraw(amnt)
        else:
            print("Account number not found!")

    def get_customer_info(self, acc_no):
        if acc_no in self.customers:
            print(self.customers[acc_no])
        else:
            print("Account number not found!")

# Example usage
bank = Bank()
bank.add_customer("Choi Seungcheol", 1002)
bank.add_customer("Yoon Jeonghan", 1004)
print()

# Perform transactions
bank.perform_deposit(1002, 5000)
bank.perform_withdrawal(1002, 150)
bank.get_customer_info(1002)
print()

bank.perform_deposit(1004, 10000)
bank.perform_withdrawal(1004, 12000)  # Insufficient funds
bank.get_customer_info(1004)
print()

# Removing a customer
bank.remove_customer(1002)
bank.get_customer_info(1002)