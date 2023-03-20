class BankAccount:
    def __init__(self, personal_id, account_type, balance=0):
        self.personal_id = personal_id
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient balance.")

    def transfer(self, amount, to_account):
        if self.balance >= amount:
            self.balance -= amount
            to_account.balance += amount
            print(f"Transferred {amount} to {to_account.personal_id}.")
        else:
            print("Insufficient balance.")

    def get_account_info(self):
        print(f"Personal ID: {self.personal_id}")
        print(f"Account type: {self.account_type}")
        print(f"Balance: {self.balance}")


accounts = {}

while True:
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. View account details")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        personal_id = input("Enter personal ID: ")
        account_type = input("Enter account type: ")
        balance = int(input("Enter initial balance: "))
        accounts[personal_id] = BankAccount(personal_id, account_type, balance)
        print("Account created successfully.")

    elif choice == 2:
        personal_id = input("Enter personal ID: ")
        amount = int(input("Enter amount to deposit: "))
        accounts[personal_id].deposit(amount)

    elif choice == 3:
        personal_id = input("Enter personal ID: ")
        amount = int(input("Enter amount to withdraw: "))
        accounts[personal_id].withdraw(amount)

    elif choice == 4:
        from_id = input("Enter personal ID to transfer from: ")
        to_id = input("Enter personal ID to transfer to: ")
        amount = int(input("Enter amount to transfer: "))
        accounts[from_id].transfer(amount, accounts[to_id])

    elif choice == 5:
        personal_id = input("Enter personal ID: ")
        accounts[personal_id].get_account_info()

    elif choice == 6:
        break

    else:
        print("Invalid choice. Try again.")
