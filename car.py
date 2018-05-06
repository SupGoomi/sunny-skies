class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price >= 10000:
            self.tax = .15
        else:
            self.tax = .12
    def displayAll(self):
        print ("Price:", self.price)
        print ("Speed:", self.speed, "mph")
        print ("Fuel:", self.fuel)
        print ("Mileage:", self.mileage, "mpg")
        print ("Tax:", self.tax)
        return self

car1 = Car(2000, 60, 'Full', 105)
car2 = Car(4000, 80, 'Half Full', 110)
car3 = Car(10000, 110, "Full", 130)
car4 = Car(15000, 120, "Full", 140)
car5 = Car(5000, 70, "Not Full", 115)
car6 = Car(120000, 150, "Full", 160)

car1.displayAll()
car2.displayAll()
car3.displayAll()
car4.displayAll()
car5.displayAll()
car6.displayAll()
