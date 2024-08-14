class Bank:
    """
    Represents a bank with a name and a list of customers.
    Method :-
        add_customer: Adds a customer to the bank.
    """

    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer ({customer.name}) added successfully to ({self.name}) Bank.")


class Customer:
    """
    Represents a customer with a name and a list of accounts.
    Method :-
        add_account: Adds an account to the customer.
        transfer: Transfers money from one account to another.
    """

    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(
            f"Account ({account.account_number}) added successfully for customer ({self.name})."
        )

    def transfer(self, from_account, to_account, amount):
        if from_account.balance >= amount:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            print(
                f"Successfully transferred ({amount}) from account ({from_account.account_number}) to account ({to_account.account_number})."
            )
        else:
            print(f"Failed to transfer ({amount}).  balance: ({from_account.balance}).")


class Account:
    """
    Represents an account with a unique account number and a balance.
    Method :-
        deposit: Adds money to the account.
        withdraw: Subtracts money from the account.
        get_balance: Returns the current balance of the account.
    """

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(
            f"Successfully deposited ({amount}) to account ({self.account_number}). New balance: ({self.balance})"
        )

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(
                f"Successfully withdrew ({amount}) from account ({self.account_number}). New balance: ({self.balance})"
            )
        else:
            print(
                f"Failed to withdraw ({amount}) from account ({self.account_number}). balance: ({self.balance})"
            )

    def get_balance(self):
        return self.balance
