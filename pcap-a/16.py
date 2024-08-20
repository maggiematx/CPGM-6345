class MyException(Exception):
    pass
try:
    raise Exception("A", "B")
except MyException:
    print("Hello", end=" ")
finally:
    print("Bye")
