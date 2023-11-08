import datetime

class Bank:
    def __init__(self):
        self.obj_accounts = BankAccount()

    def bank_check_password(self, acc_name, input_password):
        if isinstance(BankAccount, acc_name):
            if self.obj_accounts.acc_check_password(input_password):
                return True
            else:
                self.obj_accounts.pass_attempts += 1
                print("password incorrect")
                return False
        else:
            print("Account does not exist")

class User:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def create_account(self):


        a

class BankAccount:
    def __init__(self, initial_balance, acc_num, password, owners):
        self.name = name
        self.balance = initial_balance
        self.dob = dob
        self.acc_num = acc_num
        self.password = password
        self.log = []
        self.pass_attempts = 0
        self.owners = owners


    def __int__(self):
        return self.balance

    def __str__(self):
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.acc_num}")

    def acc_check_password (self, password):
        if password != self.password:
            print("incorrect password")
            return False
        else:
            return True

    def credit(self, how_much):
        self.balance += how_much
        self.log_event(f"credited {how_much}; new balance {self.balance}")

        return self.balance

    def debit(self, how_much):
        if self.balance < how_much:
            print(f"transaction denied, not enough balance")
        else:
            self.balance -= how_much
            self.log_event(f"debited {how_much}; new balance {self.balance}")

    def transfer_out(self, how_much, where_to):
        if self.balance >= how_much:
            self.balance -= how_much
            where_to.credit(how_much)
            self.log_event(f"transfered {how_much} to the account {where_to.acc_num}; new balance {self.balance}")
        else:
            print(f"transaction denied, not enough balance")

    def check_balance(self):
        print(f"Your balance is {self.balance}")

    def freeze_account(self):
        ...

    def log_event(self, param):
        self.log.append(
            f"{datetime.datetime.now()}: {param}")
        pass

my_bank = Bank()

def login():
    acc_name = input("Please enter your account name")
    password =  input("Please enter your password")

    if Bank.bank_check_password.
        print("access granted")

    else:
        pass



my_user = User("maya",20070328)

my_account = BankAccount(acc_num=1234, initial_balance=10, password="hello")
new_account = BankAccount(name="name", acc_num=5678, initial_balance=10, dob="20070328")

print(my_account.log)
print(new_account.log)

def login():
    print("Please enter your account name")