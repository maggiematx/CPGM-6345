# (a)
# list_3 = [x*x*x for x in range(11,22)]
# print(list_3)

# (b) 
# list_4=[]
# for x in range(3,30):
#     list_4.append(3*x)
# print(list_4)

# (c)
# list_5=[]
# for x in range (1,20):
#     if x%2==0:
#         list_5.append(x)
# print(list_5)

# (d)
n= int(input("Please enter a positive integer: "))
nfactors = [x for x in range(1, n + 1) if n % x == 0]
print("Factors of", n, ":", nfactors)

# (e)
# L = [x for x in range(20) if x not in [12, 8, 3, 17]]
# print(L)
