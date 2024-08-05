# f=open("pythonD.txt","w+")
# f.write("I love programming.\n")
# f.write("Python is the most powerful programming language.")
# # f.seek(0)
# # print(f.readline())
# # print(f.readline())
# # f.seek(0)
# # print(f.readline(5))
# # f.seek(0)
# print(f.readlines())

# f= open('xyz.txt', 'w+')
# a = [1,2,3,4,5]
# for m in a:
#    f.write(str(m))
# f.seek(0)
# for m in a:
#    print(f.read())

# try:
#     file = open('python.txt', 'r')
#     for data in file:
#             print(data)
# except:
#              print('Something went wrong!')

# file = open('data.txt', 'w+')
# print('Name of the file: ', file.name)
# s = 'Peter Wellert\nHello everybody'
# file.write(s)
# file.seek(0)
# for line in file:
#         print(line)
# file.close()

text = """Plano is a city in north Texas.
The Heritage Farmstead Museum is a restored 19th-century farm with original tools.
The Interurban Railway Museum traces the history of the Texas Electric Railway.
"""

# Write the text to the file
file = open('p.txt', 'w')
file.write(text)
file.close()

try:
    # Open the file for reading
    file = open('p.txt', 'r')
    
    # Uncomment one of the following lines to see different outputs
    # data = file.read()  # Read the entire file
    # data = file.readline()  # Read only one line
    data = file.readlines()  # Read every line, but as a list
    # data = file.readline(6)  # Read the first 6 characters of the first line
    
    print(data)
    file.close()
except Exception as e:
    print('Something went wrong!', e)
# f = open('xyz', 'w')
# for i in range(1, 6):
#         f.write(str(i) + '. Line\n')
# f = open('xyz', 'rt') 
# data = f.read()
# print(data)
