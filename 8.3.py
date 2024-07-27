class ThermostatError(Exception):
    pass

class MoistureError(Exception):
    pass

def check_temp(temperature):
    room_temp = 72
    if temperature < room_temp:
        raise ThermostatError("Indoor plants need to live at room temperature!")
    else:
        m = int(input("Enter moisture level: "))
        check_moisture(m)

def check_moisture(m):
    if m < 40:
        raise MoistureError("They also need to live at 40 percent moisture.")
    else:
        print("Plant lives!")

try:
    temperature = int(input("Enter temperature: "))
    check_temp(temperature)
except ThermostatError as te:
    print(te)
except MoistureError as me:
    print(me)