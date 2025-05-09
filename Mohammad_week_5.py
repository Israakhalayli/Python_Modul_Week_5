#Question 1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Create an instance of Rectangle
rect = Rectangle(5, 7)

# Print area and perimeter
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

## Question 2
class School:
    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students = []  # List of dictionaries: {"name": ..., "class": ...}
        self.teachers = {}  # Dictionary: {"teacher_name": "branch"}

    def add_new_student(self, student_name, student_class):
        self.students.append({"name": student_name, "class": student_class})
        print(f"Student '{student_name}' added to class '{student_class}'.")

    def add_new_teacher(self, teacher_name, branch):
        self.teachers[teacher_name] = branch
        print(f"Teacher '{teacher_name}' added with branch '{branch}'.")

    def view_student_list(self):
        print("Student List:")
        for student in self.students:
            print(f"- {student['name']} (Class: {student['class']})")

    def view_teacher_list(self):
        print("Teacher List:")
        for teacher, branch in self.teachers.items():
            print(f"- {teacher} (Branch: {branch})")

# Example usage:
school = School("Green Valley School", 1998)
school.add_new_student("Alice", "5A")
school.add_new_student("Bob", "6B")
school.add_new_teacher("Mr. Smith", "Mathematics")
school.add_new_teacher("Ms. Johnson", "English")

school.view_student_list()
school.view_teacher_list()

## Question 3
# Base class
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

# Rectangle class inherits from Shape
class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height

# Square class inherits from Shape
class Square(Shape):
    def calculate_area(self):
        # For a square, width and height should be equal
        if self.width != self.height:
            print("Warning: Width and height are not equal in this square. Using width as side length.")
        return self.width * self.width

# Create a Rectangle instance
rectangle = Rectangle(5, 7)
print("Rectangle Area:", rectangle.calculate_area())

# Create a Square instance
square = Square(4, 4)
print("Square Area:", square.calculate_area())

##Question 4
# Base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Subclass for Off-Road Vehicle (SUV)
class OffRoadVehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive

    def display_info(self):
        super().display_info()
        print(f"Four-Wheel Drive: {'Yes' if self.four_wheel_drive else 'No'}")

# Subclass for Sports Car
class SportsCar(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed

    def display_info(self):
        super().display_info()
        print(f"Max Speed: {self.max_speed} km/h")

# Create instances
suv = OffRoadVehicle("Toyota", "Land Cruiser", 2022, True)
sports_car = SportsCar("Ferrari", "488 GTB", 2020, 330)

# Display their information
print("Off-Road Vehicle Info:")
suv.display_info()

print("\nSports Car Info:")
sports_car.display_info()

##Question 5
# Customer class
class Customer:
    def __init__(self, name, surname, tc_identification, phone):
        self.name = name
        self.surname = surname
        self.tc_identification = tc_identification
        self.phone = phone

    def display_information(self):
        print("Customer Information:")
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"TC Identification: {self.tc_identification}")
        print(f"Phone: {self.phone}")

# Account class inherits from Customer
class Account(Customer):
    def __init__(self, customer, account_number, balance=0.0):
        # Inherit customer information
        super().__init__(customer.name, customer.surname, customer.tc_identification, customer.phone)
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f} successfully.")
        else:
            print("Deposit amount must be positive.")

    def money_check(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount:.2f} successfully.")
        else:
            print("Insufficient funds. Withdrawal cancelled.")

    def display_balance(self):
        print(f"Account Balance: {self.balance:.2f} TL")

# Example usage
customer1 = Customer("Ahmet", "Yılmaz", "12345678901", "+90 531 000 0000")

# Create an account for the customer
account1 = Account(customer=customer1, account_number="TR00123456789", balance=1000)

# Display customer info
account1.display_information()

# Perform some transactions
account1.deposit(500)
account1.money_check(300)
account1.money_check(1500)  # Should show insufficient funds
account1.display_balance()
