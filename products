class product(object):
    def __init__(self, price, item_name, weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def tax(self, tax):
        self.price += self.price * tax
        return self
    def return_item(self, reason_for_return):
        if reason_for_return == "defective":
            self.price = 0
            self.status = "defective"
        elif reason_for_return == "like new":
            self.status = "for sale"
        elif reason_for_return == "opened":
            self.status = "open"
            self.price = self.price - (self.price*.2)
        return self
    def displayInfo(self):
        print ("Price:", self.price)
        print ("Item Name:", self.item_name)
        print ("Weight:", self.weight, "lbs")
        print ("Brand:", self.brand)
        print ("Status:", self.status)
        return self
apples = product(4, "Bag of Apples", 3, "Market Pantry", "for sale")
cereal = product(3, "Cheerios", 1, "General Mills", "for sale")
ice_cream = product(5, "Vanilla Ice Cream", .5, "Blue Bunny", "for sale")
apples.sell().tax(.09).displayInfo()
cereal.tax(.09).displayInfo()
ice_cream.sell().tax(.09).displayInfo()
