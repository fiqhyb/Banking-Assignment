from customer import Customer
class Bank(object):
    def __init__(self,customers,numcustomer,bankName):
        self.customers = customers
        self.numcustomer = int(numcustomer)
        self.bankName = str(bankName)

    def addCustomer(self):
        clist=[]
        cust = Customer(input("First Name :"),
                        input("Last Name  :"),
                        input("Starting Balance :"))
        clist.append(Customer.getFirstname(cust))
    def getNumOfCustomers(self):
        return self.numcustomer
    def getCustomer(self):
        return Customer
    def toString(self):
        print  ("### {0} Bank ###\n"
                "Customers :{1}\n"
                "Number of Customer :{2}"
                .format(self.bankName,self.customers,self.numcustomer))