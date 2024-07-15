class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name, "is open!")


obj1 = Restaurant("La Madeleine", "French")
obj2 = Restaurant("Panera Bread", "American")

obj1.describe_restaurant()
#obj1.open_restaurant()
obj2.describe_restaurant()
#obj2.open_restaurant()
