class InsufficientFundsError(Exception):
    def __str__(self):
        return "Your current balance is less than your desired withdrawal amount\nor you entered the negative withdrawal amount!"

class BankApplication:
    print("Welcome to the Robust Banking System!")
    def __init__(self):
        self.bank={}
        
    def create_account(self):
        self.acc_number=input("\nEnter the your account number:")
        for i in self.bank:
            while int(self.acc_number)==i:
                print("\nPlease enter your account number\nyour entered account number is associated with another person!")
                self.acc_number=input("\nEnter the your account number:")
        while len(self.acc_number)<5:
            print("Please enter the entire your account number!")
            self.acc_number=input("\nEnter the your account number:")
        self.acc_name=input("Enter the your name:")
        self.acc_balance=int(input("Enter initial deposit amount:"))
        assert int(self.acc_balance)>=0, "You have to enter the positive amount!"
        print("Account Created Successfully!")
        self.bank[int(self.acc_number)]=[self.acc_name,self.acc_balance]

    def deposit_funds(self):
        if self.bank=={}:
            print("\nPlease create the bank account first!")
        else:
            acc_number=input("\nWhich account number's balance you want to check:")
            while len(acc_number)<5:
                print("\nPlease enter the entire account number!")
                acc_number=input("\nWhich account number's balance you want to check:")
            try:
                found=None
                for i in self.bank:
                    if int(acc_number)==i:
                        found=i
                
                if found==None:
                    print("\nYour entered account number is not found in the system!")
                
                if found!=None:
                    amount=int(input("\nEnter the amount which you want to deposit from your account:"))
                    
                    assert amount>0
            except AssertionError:
                print("Please enter the positive number!")
            else:
                if found!=None:
                    self.bank[found][1]+=amount
                    print(f"Deposit Succssful!")
            finally:
                if found!=None:
                    print(f"\nYour new balance is {self.bank[found][1]}")

    def withdraw_funds(self):
        if self.bank=={}:
            print("\nPlease create the bank account first!")
        else:
            acc_number=input("\nWhich account number's balance you want to check:")
            
            while len(acc_number)<5:
                print("\nPlease enter the entire account number!")
                acc_number=input("\nWhich account number's balance you want to check:")
            try:
                found=None
                
                for i in self.bank:
                    if i==int(acc_number):
                        found=i
                
                if found==None:
                    print("\nYour entered account number is not found in the system!")
                
                if found!=None:
                    amount=int(input("\nEnter the amount which you want to withdraw from your account:"))
                
                    if amount>int(self.bank[found][1]) or amount<0:
                        raise InsufficientFundsError
            except InsufficientFundsError as e:
                print(e)
            else:
                if found!=None:
                    self.bank[found][1]-=amount
                    print(f"\nWithdrawal successful!")
            finally:
                if found!=None:
                    print(f"\nYour new balance is {self.bank[found][1]}")
                
    def check_balance(self):
        if self.bank=={}:
            print("\nBank has no records!")
        else:
            acc_number=input("\nWhich account number's balance you want to check:")
            while len(acc_number)<5:
                print("\nPlease enter the entire account number!")
                acc_number=input("\nWhich account number's balance you want to check:")
            found=None
            for i in self.bank:
                if int(acc_number)==i:
                    found=self.bank[i]
            if found==None:
                print("Your entered account number is not found in the system!")
            if found!=None:
                print(f"\nCurrent Balance in your account:{found[1]}")
            
    def check_records(self):
        print()
        for i,j in self.bank.items():
            print(f"Account Number: {i}, Account Holder Name:{j[0]}, Current Balance:{j[1]}")

    def ask_user(self):
        while True:
            print("\nPlease select an option:")
            print("1. Create Account")
            print("2. Deposit Funds")
            print("3. Withdraw Funds")
            print("4. Check Balance")
            print("5. Check Account Details")
            print("6. Exit")
            choice=int(input("Enter your choice:"))

            if choice==1:
                self.create_account()
            elif choice==2:
                self.deposit_funds()
            elif choice==3:
                self.withdraw_funds()
            elif choice==4:
                self.check_balance()
            elif choice==5:
                self.check_records()
            elif choice==6:
                break
            else:
                print("Please enter the valid choice!")

obj=BankApplication()
obj.ask_user()