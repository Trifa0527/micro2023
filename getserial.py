import serial

ser = serial.Serial("COM3", 115200, timeout = 1)

def get():
    if ser.readable():
        orgdata = ser.readline()
        data = orgdata.split('%%')
    elif ser.readable() == 0:
        return 0
    return data