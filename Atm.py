from credentials import ids, passwords 
from customer import Customer

line = '-----------------------------------'
cust = Customer(954616, "Felix", "Bedenhost", 'Male', 78456216, "Manzini Eswatini")
customers_list = []

#A method to start the program
def start():    
    print(f"{line} \n Welcome to Our ATM System \n {line}")
    choice = int(input("Choose what to do below: \n1 ----- Admin Login\n2 ----- Cashier Login\n3 ----- Customer Login\n"))
    if choice == 1:
        adminLogin()
    elif choice == 2:
        cashierLogin()
    elif choice  == 3:
        customerLogin()
    else:
        print("Wrong choice!")

def adminLogin():
    admin = Admin(85005, "Lutfo", "Dlamini", 'M', "administrator", 78491526, 'mail@google.com')
    admin.login()
def cashierLogin():
    cash = Cashier()
    cash.login()
def customerLogin():
    cust.login()


class Employee:
 
    def __init__(self, emp_id, first_name, last_name, gender, job_title, contact_number, email_address):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.job_title = job_title
        self.contact_number = contact_number
        self.email_address = email_address
        
    def login(self):
        print(line)
        id = input("Enter Your login id : ")
        password = input("Enter Your password: ")
        if self.searchList(id, ids) and self.searchList(password, passwords):
            admin = Admin(85005, "Lutfo", "Dlamini", 'M', "administrator", 78491526, 'mail@google.com')
            admin.displayMenu()
        else:
            print("Credentials mismatch!")

    def searchList(self, id, lst):
        for i,(k, v) in enumerate(lst.items()):
            if i == len(ids):
                return False
            elif v == id:
                return True
        
        

class Admin(Employee):
    employees = []

    def __init__(self, emp_id, first_name, last_name, gender, job_title, contact_number, email_address):
        super().__init__(emp_id, first_name, last_name, gender, job_title, contact_number, email_address)
    def displayMenu(self):
        choice = int(input(f'{line}\nChoose what to do below\n1 ---- Find Employees\n2 ---- Find Customers \n3 ---- Add Employees\
                       \n4 ---- Display All Employees\n5 ---- List Customers\n0 --- Exit\n'))
        if choice == 1:
            self.findEmployee()
        elif choice == 2:
            self.findCustomer()
        elif choice == 3:
            self.createEmployee()
        elif choice == 4:
            self.listEmployees()
        elif choice == 5:
            self.listCustomers()
        elif choice == 0:
            exit(1)

    def findEmployee(self):
        print('Finding Employee')
    def findCustomer(self):
        cust_id = input('Enter customer id to find: ')
        print(f'Your entered this id to find : {cust_id}')
    def listEmployees(self):
        print('Emp ID\tFirst Name\tLast Name\tGender\tJob Title\tContact\tEmail')
        for i in self.employees:
            print(f'{i.emp_id}\t {i.first_name} {i.last_name}\t {i.gender} {i.job_title} {i.contact_number} {i.email_address}')
    def listCustomers(self):
        print('Listing customers')


    def createEmployee(self):
        print(f'{line} \nCreating new Employee\n')
        id = int(input("Enter Employee id: "))
        firstname = input("Enter first name: ")
        lastname = input("Enter last name: ")
        gender = input("Enter gender: ")
        jobtitle = input("Enter job title: ")
        contact = input("Enter contact: ")
        email = input ("Enter email Address : ")
        self.new_emp = Employee(id, firstname, lastname, gender, jobtitle, contact, email)#Created employee can be saved into a text file
        self.employees.append(self.new_emp)
        print(f'New Employee created as : \nId\tName\tSurname\tGender\tContact\tJob\
            \n{id} {firstname} {lastname} {gender} {contact} {jobtitle}')
        next_transaction = input('Do you want to perform another transaction? Y/N ')
        if next_transaction.lower() == 'y':
            self.displayMenu()
class Cashier:
    def displayMenu(self):
        choice = input(f'{line}\n Choose what to do below\n1 -------- Find Account\n2 -------- Find Customer\n3 -------- Make Deposit\
                       \n4 -------- Make Withdrawal\n5 -------- Make Transfere\n0 -------- Exit\n')
        if choice == '1':
            self.findAccount()
        elif choice == '2':
            cust_id = input('Enter an id to find: ')
            for i in customers_list:
                if i.customerid == cust_id:
                    print('Customer Details:\tName {i.firstname}')
        elif choice == '3':
            acc = input('Enter account number to make deposit: ')
            print(f'You have entered this acc {acc}')            
        else:
            print('Wrong choice!')
    def login(self):
        login = input('Enter your login: ')
        passw = input('Enter your password: ')
        if login == '10001' and passw == 'passc': #Subject to change (take credentials from file)
            self.displayMenu()
        else:
            print('Wrong credentials')
    def findAccount(self):
        print('Finding account')
    def makeWithdrawal(self):
        #This should at least make a track to the customer in like (cust.deposit, cust. withdraw)
        print('Witdrawing Money from customer account')

            
if __name__ == "__main__":
    start()