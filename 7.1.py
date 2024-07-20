a = lambda x,y: x+y

b = lambda x: x*2

def func(a,b,c):

    return a(b(c[0]),b(c[1]))

print(func(a,b,[2,3]))