class Customer:
    def __init__(self,name,surname,tc_identification,phone):
        self.name=name
        self.surname=surname
        self.tc_identification=tc_identification
        self.phone=phone
    def display_information(self):
            print(f"Name: {self.name}")
            print(f"Surname: {self.surname}")
            print(f"TR ID: {self.tc_identification}")
            print(f"Phone: {self.phone}")
        


class Account(Customer):
    def __init__(self, name, surname, tc_identification, phone,account_number,balance):
        self.account_number=account_number
        self.balance=balance
        super().__init__(name, surname, tc_identification, phone)
    
    def deposit(self, amount):
         self.balance+=amount
         print(f"Deposited {amount} . New balance: {self.balance} ")
    
    def money_check(self, amount):
         if self.balance >= amount:
              self.balance -=amount
         else:
              print("Insufficient balance")
    
    def display_balance(self):
         print(f"Account balance: {self.balance}")



account1 = Account("Asem", "Asda", "12345678900", "0555-123-4567", "TR001", 50000)

# Use inherited and custom methods
account1.display_information()
account1.display_balance()
account1.deposit(1000)
account1.money_check(3000)
account1.display_balance()