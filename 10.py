# name = 'silly walks'
# for character in name:
#     print(character, end=' ')
# print()


# name= 'silly walks' 
# for x in range(len(name)): 
#     print(name[x], end=' ') 

# alphabet =abcdefghijklmnopqrstuvwxyz"
# del alphabet[0] 
# alphabet.append("A") 

# Demonstrating min() - Example 1:
# print(min("aAbByYzZ"))
# # Demonstrating min() - Examples 2 & 3:
# t = 'The Knights Who Say "Ni!"'
# print('[' + min(t) + ']')
# t = [0, 1, 2]
# print(min(t))

# # Demonstrating max() - Example 1:
# print(max("aAbByYzZ"))
# # Demonstrating max() - Examples 2 & 3:
# t = 'The Knights Who Say "Ni!"'
# print('[' + max(t) + ']')
# t = [0, 1, 2]
# print(max(t))

# # Demonstrating the index() method:
# print("aAbByYzZaA".index("b"))
# print("aAbByYzZaA".index("Z"))
# print("aAbByYzZaA".index("A"))

# # Demonstrating the list() function:
# print(list("abcabc"))
# # Demonstrating the count() method:
# print("abcabc".count("b"))
# print('abcabc'.count("d"))

# print('[' + 'alpha'.center(10) + ']')

# # Demonstrating the endswith() method:
# if "epsilon".endswith("on"):
#     print("yes")
# else:
#     print("no")


# t = "zeta" 
# print(t.endswith("a")) 
# print(t.endswith("A")) 
# print(t.endswith("et")) 
# print(t.endswith("eta")) 

# # Demonstrating the find() method:
# print("Eta".find("ta"))
# print("Eta".find("mma"))

# print('lambda30'.isalnum())
# print('lambda'.isalnum())
# print('30'.isalnum())
# print('@'.isalnum())
# print('lambda_30'.isalnum())
# print(''.isalnum())

mystr = '12345' 
print(mystr.isdigit())
mystr = '10.5' 
print(mystr.isdigit())
mystr = 'python' 
print(mystr.isdigit())