class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def display(self):
        print ("Price:",self.price)
        print ("Max Speed:",self.max_speed)
        print ("Miles:",self.miles)
        return self
    def ride(self):
        self.miles+=10
        return self
    def reverse(self):
        if self.miles<=5:
            self.miles=0
        else:
            self.miles-=5
        return self

bike_1 = Bike(200, 150, 100000)
bike_2 = Bike(100, 100, 200000)
bike_3 = Bike(350, 175, 150000)
bike_1.ride().ride().ride().reverse().display()
bike_2.ride().ride().reverse().reverse().display()
bike_3.reverse().reverse().reverse().display()
