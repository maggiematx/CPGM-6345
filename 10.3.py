try:
    
file = open('data.txt', 'r')

 # Insert your code here
    data = file.read()
    
     print(data)

except:

    print('Something went wrong!')