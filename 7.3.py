# (a) 
L=[x + 1 for x in [2, 4, 6, 8]]
print(L)

# (b) 
L=[10*x for x in range(5, 10)]
print(L)

# (c) 
L=[x for x in range(10, 21) if x % 3 == 0]
print(L)

# (d) 
L=[(x, y) for x in range(3) for y in range(4)]
print(L)

# (e) 
L=[(x, y) for x in range(3) for y in range(4) if (x + y) % 2 == 0]
print(L)