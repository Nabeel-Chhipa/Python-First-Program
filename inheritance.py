class Car:
    def __init__(self):
        self.wheels = 4
        self.seats = 4

    def drive(self):
        print('Driva a normal car')

class SportsCar(Car):
    def __init__(self):
        super().__init__()
        self.enginePower = '600 hp'
        self.seats = 2
    
    def drive(self):
        print('Drive a sports car')

normalCar = Car()
print(normalCar.seats)