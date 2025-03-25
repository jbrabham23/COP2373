class BankAcct:
    # Initialize the bank account with name, account number, balance, and interest rate
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    # Method to adjust the interest rate of the account
    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate
        print(f"Interest rate adjusted to: {self.interest_rate}%")

    # Method to withdraw a specified amount from the account
    def withdraw(self, amount):
        # Check if there is insufficient funds
        if amount > self.amount:
            print("Insufficient funds.")
        else:
            self.amount -= amount
            print(f"Withdrew: {amount}. New balance: {self.amount}")

    # Method to deposit a specified amount into the account
    def deposit(self, amount):
        self.amount += amount
        print(f"Deposited: {amount}. New balance: {self.amount}")

    # Method to return the current balance of the account
    def get_balance(self):
        return self.amount

    # Method to calculate the interest earned over a specified amount of days
    def calculate_interest(self, days):
        interest = (self.amount * self.interest_rate * days) / 36500
        return interest

    # String representation method to display account details
    def __str__(self):
        return (f"Account holder: {self.name}\nAccount number: {self.account_number}"
                f"\nBalance: ${self.amount: .2f}\nInterest Rate: {self.interest_rate}%")

# Test function to validate the methods in the BankAcct class
def test_bank_acct():
    # Creating an account
    account = BankAcct("Jadyn Brabham", "123456789", 1000, 5)

    # Display initial account information
    print(account)

    # Test depositing money
    account.deposit(500)

    # Test withdrawing money
    account.withdraw(100)

    # Test adjusting the interest rate
    account.adjust_interest_rate(8)

    # Test calculating interest for 30 days
    interest = account.calculate_interest(30)
    print(f"Interest earned in 30 days: ${interest: .2f}")

    # Display final account information
    print(account)

# Run the test function
test_bank_acct()