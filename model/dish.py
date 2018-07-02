class Dish():
    def __init__(self):
        self.restaurant = None
        self.id = None
        self.name = None
        self.description = None
        self.price = None

    def getRestaurant(self):
        return self.restaurant

    def setRestaurant(self, restaurant):
        self.restaurant = restaurant

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price= price
