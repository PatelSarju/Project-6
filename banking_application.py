class InsufficientFundsError(Exception):
    pass

class BankApplication:
    print("Welcome to the Robust Banking System!")
    def __init__(self):
        self.bank={}
        
    def create_account(self):
        self.acc_name=input("\nEnter the your name:")
        self.acc_balance=int(input("Enter initial deposit amount:"))
        assert self.acc_balance>=0, "You have to enter the positive amount!"
        print("Account Created Successfully!")
        self.bank[self.acc_name]=self.acc_balance

    def deposit_funds(self):
        if self.bank=={}:
            print("\nPlease create the bank account first!")
        else:
            amount=int(input("\nEnter the amount which you want to deposit from your account:"))
            try:
                amount<0
            except:
                print("Please enter the positive number!")
            else:
                self.acc_balance+=amount
                print(f"Deposit Succssful!")
            finally:
                print(f"Your new balance is {self.acc_balance}")

    def withdraw_funds(self):
        if self.bank=={}:
            print("\nPlease create the bank account first!")
        else:
            amount=int(input("\nEnter the amount which you want to withdraw from your account:"))
            try:
                amount>self.acc_balance
            except InsufficientFundsError:
                print("Your balance is not enough for your desired withdrawal amount!")
            else:
                self.acc_balance-=amount
                print(f"Withdrawal successful!")
            finally:
                print(f"Your new balance is {self.acc_balance}")

    def check_balance(self):
        if self.bank=={}:
            print("\nPlease create the bank account first!")
        else:
            print(f"Your current balance is {self.acc_balance}!")

    def ask_user(self):
        while True:
            print("\nPlease select an option:")
            print("1. Create Account")
            print("2. Deposit Funds")
            print("3. Withdraw Funds")
            print("4. Check Balance")
            print("5. Exit")
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
                break
            else:
                print("Please enter the valid choice!")

obj=BankApplication()
obj.ask_user()