class Vehicle:
     def __init__(self, make, model,year):
           self.make=make
           self.model=model
           self.year=year


class OffRoadVehicle(Vehicle):
       def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive
      
class SportsCar(Vehicle):
     def __init__(self, make, model, year,max_speed):
          super().__init__(make, model, year)
          self.max_speed=max_speed


off_road = OffRoadVehicle("Toyota", "and Cruiser", 2021, True)
sports_car = SportsCar("Ferrari", "488", 2022, 330)


print("Off-Road Vehicle:")
print(f"Make: {off_road.make}, Model: {off_road.model}, Year: {off_road.year}, Four-Wheel Drive: {off_road.four_wheel_drive}\n")


print("Sports Car:")
print(f"Make: {sports_car.make}, Model: {sports_car.model}, Year: {sports_car.year}, Max Speed: {sports_car.max_speed} km/h")