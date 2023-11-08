import datetime
import bank_main
import hashlib


my_account = bank_main.BankAccount(
    owners="Maya",
    acc_num=1234,
    password="hello")

new_account = bank_main.BankAccount(
    owners="name",
    acc_num=5678,
    password="byebye")

test_bank = bank_main.Bank(accounts=[my_account, new_account])

test_account = bank_main.BankAccount(1234, [my_account])
test_account.set_password('password')

another_account = bank_main.BankAccount(5678, [my_account])
another_account.set_password('qwerty')


def login():

    acc_number = int(input("Please enter your account number"))
    password = hashlib.sha3_256((input("Please enter your password")).encode()).hexdigest()

    selected_account = test_bank.get_account(acc_number)
    global selected_account

    if test_bank.bank_check_password(selected_account, password):
        print("access granted")
        return True

    else:
        return False  # validating the account => change to user later (why do I keep thinking of things?!)


# selected_account: bank.BankAccount | None = None
# ==> what does this mean?

while True:
    verified = login()

    while verified:
        if selected_account:
            # Show actions for a selected account
            print(f'Selected account is {selected_account} with balance {selected_account.balance}')

            print(
                'Actions are:'
                '1: Credit money'
                '2: Debit money'
                '3: Balance enquiry'
                '4: Set password'
            )

            action = input('Action:')
            pwd = input('Password:')

            if action == '1':
                amount = float(input('How much?'))
                # test_bank.credit(selected_account, amount) => for when user not account and bank does transactions
                selected_account.credit(amount)

            elif action == '2':
                amount = float(input('How much?'))
                # test_bank.debit(selected_account, amount) => for when user not account and bank does transactions
                selected_account.credit(amount)

            elif action == '3':
                balance = selected_account.check_balance(selected_account)
                print(f'Balance is {balance}')

            elif action == '4':
                new_pwd = input('New password:')
                selected_account.set_password(selected_account, new_pwd)
            else:
                print("Action does not exist")  # => add proper validation in future
        else:
            pass

        # ↓ Not applicable until accounts are assigned to a user -- needs some sort of relationship

        # else:
        #     # Actions if an account is not yet selected
        #
        #     print(
        #         'Actions are:'
        #         '1: Select an account to interact with'
        #         '2: Create an account'
        #         '3: Delete an account'
        #     )
        #
        #     action = input('Action:')
        #     if action == '1':
        #         account_number = int(input('Account number'))
        #         pwd = input('Password:')
        #         account = test_bank.get_account(account_number)
        #
        #         if account:
        #             authenticated = test_bank.authenticate(account, pwd)
        #             if authenticated:
        #                 print('Authenticated')
        #                 selected_account = account
        #             else:
        #                 print('Authentication failure')
        #                 selected_account = None
        #
        #         else:
        #             selected_account = None
        #             print('Not found. Try again')
        #
        #     elif action == '2':
        #         ...
        #     elif action == '3':
        #      ...

