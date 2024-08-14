################### Q1 ##########################
from modules.classs.Bank import Bank, Customer, Account

# test bank
bank = Bank("MS")
print(bank.name)  # MS

# test customer
customer = Customer("Mazen Saad")
print(customer.name)  # Mazen Saad

# test bank add customer
bank.add_customer(customer)  # Customer (Mazen Saad) added successfully to (MS) Bank.

# test account
account1 = Account(123456, 1000)
account2 = Account(789012, 500)
print(account1.account_number)  # 123456
print(account2.account_number)  # 789012
print(account1.balance)  # 1000
print(account2.balance)  # 500

# test customer
customer.add_account(
    account1
)  # Account (123456) added successfully for customer (Mazen Saad).
customer.add_account(
    account2
)  # Account (789012) added successfully for customer (Mazen Saad).


# test account
account1.deposit(
    200
)  # Successfully deposited (200) to account (123456). New balance: (1200)
account2.deposit(
    200
)  # Successfully deposited (200) to account (789012). New balance: (700)


account1.withdraw(
    500
)  # uccessfully withdrew (500) from account (123456). New balance: (700)
account2.withdraw(
    500
)  # Successfully withdrew (500) from account (789012). New balance: (200)

account1.withdraw(1500)  # Failed to withdraw (1500) from account (123456).
account2.withdraw(1500)  # Failed to withdraw (1500) from account (789012).


print(account1.get_balance())  # 700
print(account2.get_balance())  # 500


# test customer
customer.transfer(
    account1, account2, 300
)  # Successfully withdrew (300) from account (123456). New balance: (400)
# Successfully deposited (300) to account (789012). New balance: (500)
# Successfully transferred (300) from account (123456) to account (789012).

customer.transfer(
    account1, account2, 1000
)  # Failed to transfer (1000).  balance: (400).
customer.transfer(account2, account1, 10)  #


################### Q2 ##########################
from modules.classs.Animal import Animal, Cat

ca1 = Animal("TOM", 1)
ca1.eat()
ca1.drink()

cat2 = Cat("Gumball", 2)
cat2.meow()
cat2.eat()
cat2.drink()
