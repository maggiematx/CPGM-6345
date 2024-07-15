class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name}: {self.cuisine_type}")

    def open_restaurant(self):
        print(self.restaurant_name, "is open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        Restaurant.__init__(self,restaurant_name,cuisine_type)
        self.flavors=flavors

    def display_flavors(self):
        print(self.restaurant_name, "has the following flavors of ice cream:")
        for flavor in self.flavors:
            print(f"{flavor}")


obj1 = Restaurant("La Madeleine", "French")
obj2 = Restaurant("Panera Bread", "American")
obj3= IceCreamStand("Amy's","Dessert", ["straberry","cotton candy", "grape", "pina colada"])

obj1.describe_restaurant()
#obj1.open_restaurant()
obj2.describe_restaurant()
#obj2.open_restaurant()

obj3.display_flavors()
