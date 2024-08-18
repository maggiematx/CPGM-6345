# file = open('data.txt', 'w+')
# s = 'Peter Wellert\nHello everybody'
# file.write(s)
# file.seek(0)
# # print(file.readlines())

# # file = open('data.txt', 'r')
# # for line in file:
# #     print(line)


# # for m in file.read():
# #     print(m)
# # file.close()


# print(file.read())


# str='*'.join('HELLO')
# print(str)
# #2
# lst=['a','b','c','d']
# l='$'.join(lst)
# print(l)
# #3
# tpl=('a','b','c','d')
# t="%".join(tpl)
# print(t)
# #4
# dic = {'Python': 1, 'Pascal': 2, 'Java': 3}
# d="@".join(dic)
# print(d)

s1 = 'Where are the snows of yesteryear?' 
s2 = s1.split() 
# print(s2[-2]) 
print(s2)

# the_list = ['Where', 'are', 'the', 'snows?'] 
# s = '*'.join(the_list)
# print(s) 


# s= 'It is either easy or impossible'
# s = s.replace('easy', 'hard').replace('im', '') 
# print(s)

# for ch in "abc123XYX":
    
#     if ch.isupper(): 
#         print(ch.lower(), end=' ')
#     elif ch.islower(): 
#          print(ch.upper(), end=' ') 
#     else:
#          print(ch, end=' ')

# s1="12"
# m=int(s1)
# print(m)
# s2 = str(m) 
# print(s1 == s2) 

from random import choice, sample 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print(choice(my_list)) 
print(sample(my_list, 5)) 
print(sample(my_list, 10)) 
