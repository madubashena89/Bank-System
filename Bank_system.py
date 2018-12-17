#class => Bankaccount
#Layers of abstraction => creat new_account, access_exsisting_
from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):
    @abstractmethod
    def create_new_acc():
        return 0


    @abstractmethod
    def authenticate():
         return 0

    @abstractmethod
    def withdraw():
          return 0


    @abstractmethod
    def deposit():
          return 0


    @abstractmethod
    def show_balance():
          return 0

class Bank_account(Account):
     def __init__(self):
         #[key][0] => name ; [key][1] => balance
        self.savingsAccounts = {}
     def create_new_acc(self, name , deposit):
          self.accountNumber = randint(100000, 999999)
          self.savingsAccounts[self.accountNumber] = [name, deposit]
          print("Account creation is successful !, Your account number is: ", self.accountNumber)

     def authenticate(self, name, accountNumber):
         if accountNumber in self.savingsAccounts.keys():
             if self.savingsAccounts[accountNumber][0] == name:
                 print( "Authentication is successful")
                 self.accountNumber = accountNumber
                 return True
             else:
                 print("Authentication is failed")
                 return False
         else:
             print("Authentication is failed!")


     def withdraw(self, withdrawAmount):
          if self.withdrawAmount > self.savingsAccounts[self.accountNumber][1]:
              print("Insufficient funds")
              print("Your savings balance is: " )
              self.show_balance()
          else:
              self.savingsAccounts[self.accountNumber][1] -= withdrawAmount
              print("Withdrawal is successful. Available balance is: ")
              self.show_balance()


     def deposit(self, depositAmount):
              self.savingsAccounts[self.accountNumber][1] += depositAmount
              print("Deposit is successful !. Available balance is: " )
              self.show_balance()


     def show_balance(self):
             print("Your account balance is: " , self.savingsAccounts[self.accountNumber][1])


User1 = Bank_account()
while True:
    print("Enter 1 to create an account: ")
    print("Enter 2 to access an existing account: ")
    print("Enter 3 to exit: ")

    userInput = int(input())
    if userInput is 1:
          print("Enter your name: ")
          name = input()
          print("Enter initial deposit:")
          deposit = int(input())
          User1.create_new_acc(name, deposit)
    elif userInput is 2:
          print("Enter your name: ")
          name = input()
          print("Enter your account number: ")
          accountNumber = int(input())
          autenticationStatus = User1.authenticate(name, accountNumber)
          if autenticationStatus is True:
            while True:
              print("Enter 1 to withdraw: ")
              print("Enter 2 to deposit: ")
              print("Enter 3 to check the available balance: ")
              print("Enter 4 to return previous menu: ")
              userInput = int(input())
              if userInput is 1 :
                print("Enter withdrawal amount: ")
                withdrawAmount = int(input())
                User1.withdraw(withdrawAmount)
              elif userInput is 2:
                print("Enter deposit amount: ")
                depositAmount = int(input())
                User1.deposit(depositAmount)
              elif userInput is 3:
                User1.show_balance()
              elif userInput is 4:
                       break
    elif   userInput is 3:
                quit()

















