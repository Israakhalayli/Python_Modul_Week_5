# Question 1
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return f'Area is {self.width*self.height}'
    def perimeter(self):
        return f'Perimeter is {(self.width+self.height)*2}'

Rectangle_1=Rectangle(5,7)
print(Rectangle_1.area())
print(Rectangle_1.perimeter())

# Question 2
class School:
    def __init__(self,name,foundation_year):
        self.name=name
        self.foundation_year=foundation_year
        self.students=[]
        self.teachers={}

    def add_new_student(self,student_name,student_class):
        self.students.append({'name':student_name,'class':student_class})
        print(f"Student {student_name} added to class {student_class}.")
        
    def add_new_teacher(self,teacher_name,branch):
        self.teachers[teacher_name] = branch
        print(f"Teacher {teacher_name} added with major {branch}.")
    
    def view_student_list(self):
        if not self.students:
            print('No students enrolled yet')
        else:
            print('List of students')
            for student in self.students:
                print(f'{student['name']} : {student['class']}')

    def view_teacher_list(self): 
        if not self.teachers:
            print('No teachers working in the school')
        else:
            print('List of teachers')
            for teacher,branch in self.teachers.items():
                print(f"{teacher} : {branch}")

school=School('pacili',2000)
school.add_new_student('israa','Grade 5')
school.add_new_student('sara','Grade 4')
school.add_new_teacher('yara','math')

school.view_student_list()
school.view_teacher_list()

# Question 3

class Shap:
    def __init__(self,width,height):
        self.width=width
        self.height=height

class Rectangle(Shap):
    def calculate_area(self):
        return self.width*self.height
    
class Square(Shap):
    def calculate_area(self):
        return self.width*self.height

rectangle=Rectangle(5,10)  
print(f"Rectangle Area: {rectangle.calculate_area()}")

square=Square(4,4)
print(f"Square Area: {square.calculate_area()}")

# Question 4
class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

class OffRoadVehicle(Vehicle):
    def __init__(self,make,model,year,four_wheel_drive):
        super().__init__(make,model,year)
        self.four_wheel_drive=four_wheel_drive

    def display_info(self):
        return f"{self.year} {self.make} {self.model}, Four-Wheel Drive: {self.four_wheel_drive}"

class SportCar(Vehicle):
    def __init__(self,make,model,year,max_speed):
        super().__init__(make,model,year)
        self.max_speed=max_speed

    def display_info(self):
        return f"{self.year} {self.make} {self.model}, Max Speed: {self.max_speed} km/h"

off_road_vehicle=OffRoadVehicle("Jeep", "Wrangler", 2022, True)
sport_car=SportCar("Ferrari", "488 GTB", 2021, 330)

print(off_road_vehicle.display_info())
print(sport_car.display_info())

# Question 5

class Customer:
    def __init__(self,name,surname,tc_identification,phone):
        self.name=name
        self.surname=surname
        self.tc_identification=tc_identification
        self.phone=phone

    def display_information(self):
        return f'customer name : {self.name} , surname: {self.surname} ,  TR ID number : {self.tc_identification} , telefone number: {self.phone}'

class Account(Customer):
    def __init__(self,name,surname,tc_identification,phone,account_number,balance):
        super().__init__(name,surname,tc_identification,phone)
        self.account_number=account_number
        self.balance=balance

    def deposit(self, amount):
        if amount > 0:
            self.balance+=amount
        else:
            print('The mount should be positive.')

    def money_check(self, amount):
        if amount<= self.balance:
            self.balance-=amount
            print(f'Withdraws {amount} New balance: {self.balance}')
        else:
            print('Insufficient funds. Transaction failed')

    def display_balance(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}"

customer = Customer("John", "Doe", "123456789", "+1234567890")
account = Account(customer.name, customer.surname, customer.tc_identification, customer.phone, "987654321", 500)

print(account.display_information())

account.deposit(200)
account.money_check(100)
account.money_check(700) 

print(account.display_balance())


        

        





        














    




