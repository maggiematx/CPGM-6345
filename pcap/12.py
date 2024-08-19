my_dict = {'a':1, 'b':2}
try:
    my_dict['c']
except IndexError:
    print('A', end=' ')
except Exception:
    print("B", end=' ')
except KeyError:
    print("C", end=' ')
