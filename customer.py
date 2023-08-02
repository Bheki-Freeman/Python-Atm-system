from credentianls import customer_ids, customer_passwords
from account import account

line = '------------------------------------------'
class Customer:
    cust_account = account()

    def login(self):
        id = input('Enter your login id: ')
        passw = input('Enter your loging password: ')
        if self.searchValue(id, customer_ids) and self.searchValue(passw, customer_passwords):
            self.displayMainMenu()
        else:
            print('Login Failure!')

    def searchValue(self, id, lst):
        for i, (k, v) in enumerate(lst.items()):
            if i == len(lst):
                return False
            elif id ==  v:
                return True
                
    def displayMainMenu(self):
        choice = int(input(f'{line} \nChoose What to do below: \n1 ------ Check balance\n2 ------ Make Deposit\n3 ------ Make Widthdrawal\
              \n4 ------ Make Transfere\n0 ------ Exit\n'))        
        if choice == 1:
            self.checkBalance()
        elif choice == 2:
            self.makeDeposit()
        elif choice == 3:
            self.makeWithdrawal()
        elif choice == 4:
            self.makeTransfere()
        elif choice == 0:
            exit(0)
        else:
            print('Wrong input!')

    def makeDeposit(self):
        self.cust_account.makeDeposit()
        next_transaction = input('Do you want to perform another transaction? Y/N ')
        if next_transaction.lower() == 'y':
            self.displayMainMenu()
        else:
            exit(0)
        pass
    def checkBalance(self):
        self.cust_account.checkBalance()
        next_transaction = input('Do you want to perform another transaction? Y/N ')
        if next_transaction.lower() == 'y':
            self.displayMainMenu()
        else:
            exit(0)
        pass
    def makeWithdrawal(self):
        self.cust_account.makeWithdrawal()
        next_transaction = input('Do you want to perform another transaction? Y/N ')
        if next_transaction.lower() == 'y':
            self.displayMainMenu()
        else:
            exit(0)
        pass
    def makeTransfere(self):
        self.cust_account.makeTransfere()
        next_transaction = input('Do you want to perform another transaction? Y/N ')
        if next_transaction.lower() == 'y':
            self.displayMainMenu()
        else:
            exit(0)
        pass
