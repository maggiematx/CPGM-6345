a = ['aBc', 'def', 'gHi']
b = list(map(lambda x: x.capitalize(), filter(lambda y: y[1].isupper(), a)))
print(b)