from account import Account
class Customer(object):
    def __init__(self,firstname,lastname,account):
        self.f=firstname.title()
        self.l=lastname.title()
        self.account=account

    def getFirstname(self):
        return self.f
    def getLastname(self):
        return self.l
    def getFullname(self):
        return self.f,self.l
    def getAccount(self):
        print("Account Name :{0} {1}"
              "\nBalance      :${2}"
              .format(self.f,self.l,self.account))
    def setAccount(self):
        fname = input("First Name :")
        lname = input("Last  Name :")
        bal   = input("Starting Balance :")
        self.f=fname
        self.l=lname
        self.account=bal