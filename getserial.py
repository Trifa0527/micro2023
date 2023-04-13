import serial

ser = serial.Serial("COM3", 115200, timeout = 1)

def get():
    if ser.readable():
        orgdata = str(ser.readline())
        data = orgdata.split('%%')
        data[0] = data[0][2:100]
        return data
    elif ser.readable() == 0:
        return 0