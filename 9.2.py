# text = """abc
# def
# ghi
# """

# file = open('abc.txt', 'w')
# file.write(text)
# file.close()

# try:
#     file = open('abc.txt', 'r')
#     data = file.read()   
#     print('Employee Recordes:') 
#     print(data)
#     file.close()
# except Exception as e:
#     print('Something went wrong!', e)

file = open('abc.txt')

for m in file.read():
    print(m)