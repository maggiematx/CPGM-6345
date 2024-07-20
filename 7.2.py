a = [1,2,3,4,5,6,7,8,9]
b = [i if i%3==0 else 0 for i in a]
print(b)