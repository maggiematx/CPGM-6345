# 1]
# str="banana"
# n=iter(str)
# print(next(n))
# # print(next(n))
# # print(next(n))
# # print(next(n))
# # print(next(n))
# # print(next(n))

#2]
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

# 3]
# class PizzaError(Exception):
#     def __init__(self, pizza, message):
#         Exception.__init__(self, message)
#         self.pizza = pizza

# class TooMuchCheeseError(PizzaError):
#     def __init__(self, pizza, cheese, message):
#         PizzaError.__init__(self, pizza, message)
#         self.cheese = cheese

# def make_pizza(pizza, cheese):
#     if pizza not in ['margherita', 'capricciosa', 'calzone']:
#         raise PizzaError(pizza, "no such pizza on the menu")
#     if cheese > 100:
#         raise TooMuchCheeseError(pizza, cheese, "too much cheese")
#     print("Pizza ready!")

# for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
#     try:
#         make_pizza(pz, ch)
#     except TooMuchCheeseError as tmce:
#         print(tmce, ':', tmce.cheese)
#     except PizzaError as pe:
#         print(pe, ':', pe.pizza)

# 4]
# fruits=["apple","kiwi","banana"]
# p=[x if x!="banana" else "orange" for x in fruits]

# print(p)

# 5]
# def foo(x): 
#            assert x 
#            return 1/x 
# try: 
#             print(foo(0)) 
# except ZeroDivisionError: 
#             print("zero")

# 6]
# def bad_fun(n):
#     raise ZeroDivisionError
# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("What happened? An error?")
# print("THE END.")

# 7]
# def bad_fun(n):
#     try:
#         return n / 0
#     except:
#         print("I did it again!")
#         raise
# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("I see!")
# print("THE END.")


# 9]
# class InvalidMarks(Exception):
#     def __init__(self,marks):
#         self.marks=marks
# try:
#     marks=int(input("enter marks scored\n"))
#     if marks<50 or marks>100:
#         raise InvalidMarks ("age does not seem appropriate")
# except ValueError:
#     print("Marks are supposed to be integer?")
# except InvalidMarks as e:
#     print(e)

# 10]
# mytuple = ("apple", "banana", "cherry")
# for x in mytuple:
#     print(x)
           

# 11]
# mystr ="banana"
# for x in mystr:
#   print(x)

# 12]
# def even(n):
#       for x in range(n):
#           if (x%2==0):
#                yield x
# num=even(10)
# for i in num :#using for loop
#    print(i)

# # print(list(num))

# print(next(num))

# 13]
# def generate_multiples(m, n):
#           count = 0
#           while count < n:
#                   yield m * count
#                   count += 1
# def main():
#        for mult in generate_multiples(3, 6):
#               print(mult, end=' ')
#        print()
# if __name__ == '__main__':
#      main()

# 14]
# def double(x):
#       return x*2
# print(double(7))
# p=lambda x:2*x
# print(p(7))

# 15]
# def add(x,y):
#     return x+y
# print(add(8,7))
# p=lambda x,y:x+y
# print(p(8,7))

# 16]
# def myfunc(n):
#      return lambda a : a * n
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# print(mydoubler(11))
# print(mytripler(11))

# 17]
# fruits = ["apple", "banana", "cherry", "kiwi","mango"] 
# newlist = [x if x!= "banana" else "orange" for x in fruits]
# print(newlist)

# 18]
# newlist = [x for x in range(10)]
# print(newlist)

# 19]
# list_1 = []
# for ex in range(6):
#     list_1.append(10 ** ex)
# list_2 = [10 ** ex for ex in range(6)]
# print(list_1)
# print(list_2)

# 20] 
# list_3 = [x*x*x for x in range(11,22)]
# print(list_3)


# 21]
# list_4=[]
# for x in range(3,30):
#     list_4.append(3*x)
# print(list_4)

# 22]
# list_5=[]
# for x in range (1,20):
#     if x%2==0:
#         list_5.append(x)
# print(list_5)

# 23]
# n= int(input("Please enter a positive integer: "))
# nfactors = [x for x in range(1, n + 1) if n % x == 0]
# print("Factors of", n, ":", nfactors)

# 24]
# L = [x for x in range(20) if x not in [12, 8, 3, 17]]
# print (L)

# 25]
# short_list =['mython', 'python', 'fell', 'on', 'the', 'floor'] 
# new_list = list(map(lambda s: s.title(), short_list)) 
# print(new_list)

# 26]
# list_1 = [x for x in range(5)]
# list_2 = list(map(lambda x: 2 ** x, list_1))
# print(list_2)
# [1, 2, 4, 8, 16]
# for x in map(lambda x: x * x, list_2):
#     print(x, end=' ')
# print()

# 27]
# data = [10,8,6,5,4,3,2,1,-1,-2,-3,-4,-5,-6]
# filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
# print(data)
# print(filtered)

# 28]
ages = [5,12, 17, 18, 24, 32]
def myFunc(x):
    if x >18:
        return False
    else:
        return True
adults = filter(myFunc, ages)
for x in adults:
    # print(x)

    print(list(adults))
