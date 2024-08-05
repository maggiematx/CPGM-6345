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

f= open('xyz.txt', 'w+')
a = [1,2,3,4,5]
for m in a:
   f.write(str(m))
f.seek(0)
for m in a:
   print(f.read())
