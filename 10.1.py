f = open('xyz', 'w')

for i in range(1, 6):

        f.write(str(i) + '. Line\n')

f = open('xyz', 'rt')

data = f.read()

print(data)

