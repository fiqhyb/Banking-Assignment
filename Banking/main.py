from bank import Bank
from account import Account
from customer import Customer

def main():
    customer = []
    print("###Bank Initialization###")
    numcust  = int(input("Number of Customer :"))
    bname    = str(input("Name of the Bank :")).title()
    binfo = Bank(customer,numcust,bname)
    binfo.toString()
    for i in range(numcust):
        print("###Customer Data###")
        fname = input("First Name :").title()
        lname = input("Last  Name :").title()
        bal   = 0
        cinfo = Customer(fname,lname,bal)
        cinfo.getAccount()
        customer.append(fname)
    binfo.toString()
    while True:
        print("### Login ###")
        user = input("Type first name to login :").title()
        if user in customer:
            jbal = Account(input("Starting Balance :"))
            while True:
                print(("###{0}###\n".format(user)+
                       "Balance :${0}\n".format(Account.getBalance(jbal))+
                       "[1] Deposit\n"+
                       "[2] Withdraw\n[Q] Quit"))
                choice = input("Enter Selection :").upper()
                if choice == "1":
                    jbal.deposit(input("Amount to Deposit :"))
                elif choice == "2":
                    jbal.withdraw(input("Amount to Withdraw :"))
                elif choice == "Q":quit()
main()