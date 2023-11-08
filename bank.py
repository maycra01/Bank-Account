import datetime

class Bank:
    def __init__(self):
        self.obj_accounts = []

    def get_account(self, acc_num: int):
        print(acc_num)
        for account in self.obj_accounts:
            print(account)
            print(acc_num)
            print(account.acc_num)
            if acc_num == account.acc_num:
                return account

            else:
                print("Account does not exist")

    def bank_check_password(self, account, input_password):
        #if isinstance(BankAccount, account):
        print(account)
        if account.acc_check_password(input_password):
            return True
        else:
            account.pass_attempts += 1
            print("password incorrect")
            return False


    def add_account(self, new_account):
        self.obj_accounts.append(new_account)

class User:
    ...


class BankAccount:
    def __init__(self, owners, initial_balance, dob, acc_num, password):
        self.owners = owners
        self.balance = initial_balance
        self.dob = dob
        self.acc_num = acc_num
        self.password = password
        self.log = []
        self.pass_attempts = 0


    def __int__(self):
        return self.balance

    def __str__(self):
        return (f"Account Holder: {self.owners}\n"
                f"Account Number: {self.acc_num}")

    def acc_check_password (self, import_password):
        if import_password != self.password:
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

def login():
    acc_number = input("Please enter your account number")
    password =  input("Please enter your password")

    account = my_bank.get_account(acc_number)

    if my_bank.bank_check_password(account, password):
        print("access granted")

    else:
        pass


my_account = BankAccount(owners="Maya", acc_num=1234, initial_balance=10, dob="20070328", password="hello")
new_account = BankAccount(owners="name", acc_num=5678, initial_balance=10, dob="20070328", password="byebye")

my_bank = Bank()

my_bank.add_account(my_account)
print(my_bank.obj_accounts)

my_bank.add_account(new_account)

print(my_bank.obj_accounts)


print(my_account.log)
print(new_account.log)


login()