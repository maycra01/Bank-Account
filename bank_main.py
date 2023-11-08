# sort out password - done
# TODO sort out CLI
# TODO make constructor and stuff prettier
# TODO attach password to user not account => allows me to complete CLI to switch between accounts
# TODO create unique object names for accounts
# TODO add a timer to lock you out of your account after a period of time

import datetime
import hashlib
import uuid


class Bank:
    def __init__(self, accounts):
        self.accounts_of_bank = accounts

    def get_account(self, acc_num: int):
        print(acc_num)
        for account in self.accounts_of_bank:
            if acc_num == account.acc_num:
                return account

            else:
                print("Account does not exist")

    def bank_check_password(self, account, input_password):
        print(account)
        if account.acc_check_password(input_password):
            return True
        else:
            account.pass_attempts += 1
            return False

    def add_account(self, new_account):
        self.accounts_of_bank.append(new_account)


class User:
    def __init__(self, first_name, last_name, dob, password):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.customerID = uuid.uuid4()  # Assigns unique ID
        self.password = hashlib.sha3_256(password.encode()).hexdigest() # hashes password (inside or outside of func?)

    def create_account(self,):  # headache for another day
        ...


class BankAccount:
    def __init__(self, owners, acc_num, password):
        self.owners = owners
        self.balance = 0
        self.doc = ""
        self.acc_num = acc_num
        self.log = []
        self.pass_attempts = 0
        self.password = password


    def __int__(self):
        return self.balance

    def __str__(self):
        return (f"Account Holder: {self.owners}\n"
                f"Account Number: {self.acc_num}")

    def acc_check_password (self, import_password):
        if import_password != self.password:
            print("Password Incorrect")
            return False
        else:
            return True

    def credit(self, how_much, origin=None):
        self.balance += how_much
        self.log_event(f"credited {how_much}; from {origin}; new balance {self.balance}"
                       if origin else f"credited {how_much}; new balance {self.balance}")

        return self.balance  # why???

    def debit(self, how_much):
        if self.balance < how_much:
            print(f"transaction denied, not enough balance")
        else:
            self.balance -= how_much
            self.log_event(f"debited {how_much}; new balance {self.balance}")

    def transfer_out(self, how_much, where_to):
        if self.balance >= how_much:
            self.balance -= how_much
            where_to.credit(how_much, self.acc_num)
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

    def set_password(self, new_password):
        self.password = new_password
        pass





new_account = BankAccount(owners="name", acc_num=5678, dob="20070328", password="byebye")

my_bank = Bank()

my_bank.add_account(my_account)
print(my_bank.accounts_of_bank)

my_bank.add_account(new_account)

print(my_bank.accounts_of_bank)


print(my_account.log)
print(new_account.log)


login()