text = """employee name, employee id, salary:
Maggie, 001, $60,000
Vinita, 002, $75,000
Justin, 003, $80,000
Kent, 004, $82,000
Alex, 005, $82,000
"""


file = open('employee.dat', 'w')
file.write(text)
file.close()

try:
    file = open('employee.dat', 'r')
    data = file.read()   
    print('Employee Recordes:') 
    print(data)
    file.close()
except Exception as e:
    print('Something went wrong!', e)



additional_text="""Abby, 006, $65,000
Eddie, 007, $54,000
Frank, 008, $90,000
"""
with open('employee.dat', 'a') as file:
        file.write(additional_text)

try:
    with open('employee.dat', 'r') as file:
        data = file.read()
    
    print("Updated Employee Records:")
    print(data)
except Exception as e:
    print('Something went wrong!', e)