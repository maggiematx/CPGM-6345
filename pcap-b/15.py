
class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)
        print("Hello", end=" ")
 
    def __str__(self):
        return "A"
 
try:
    raise MyException("B")
except Exception as e:
    print(e)