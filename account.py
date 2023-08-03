class account:
    # account_number, customer_id, account_name, acount_type, balance, date_created
    balance = 0.0
    foreign_balance = 0.0

    def __init__(self) -> None:
        pass
    def assignAttributes(self, accountnumber, customerid, accountname, accounttype, balance, datecreated):
        self.account_number = accountnumber
        self.customer_id = customerid
        self.acount_name = accountname
        self.account_type = accounttype
        self.balance = balance
        self.date_created = datecreated
    
    def checkBalance(self):
        print(f'The available balance is {self.balance}')
    def makeDeposit(self):
        dep  = float(input('Enter the deposit: '))
        self.balance += dep
        print(f'Successfully deposited {dep} \nNew balance is {self.balance}\n')
    def makeWithdrawal(self):
        wit_amount = float(input('Enter amount to withdraw: '))
        self.balance -= wit_amount
        print(f'Withdrawal Successful\nNew balance is {self.balance}\n')
    def makeTransfere(self):
        acc_number = int(input('Enter account number: '))
        trans_amount = float(input('Enter amount : '))
        self.foreign_balance += trans_amount
        self.balance -= trans_amount
        print(f'Transfere successful!\nNew balance is {self.balance}\n')
