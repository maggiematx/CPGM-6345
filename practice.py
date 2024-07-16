# class InventoryError(Exception):
#     pass

# class LocationtooFarError(Exception):
#     pass

# def schedule_delivery(distance):
#     if distance > 10:
#         raise LocationtooFarError("delivery available within 10 miles only")
#     else:
#         print("order placed")

# def check_order(q):
#     stock = 100
#     if q > stock:
#         raise InventoryError("insufficient stock")
#     else:
#         d = int(input("enter distance from store?\n"))
#         schedule_delivery(d)

# try:
#     quantity = int(input("enter required quantity?\n"))
#     check_order(quantity)
# except InventoryError as ie:
#     print(ie)
# except LocationtooFarError as le:
#     print(le)

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese

def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)