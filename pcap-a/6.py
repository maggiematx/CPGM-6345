try:
    if '1' != 1:  
          raise FirstError
    else:
        print('FirstError has not occured.')
except FirstError:
    print('FirstError has occured.')
else:
    print('None of the above.')