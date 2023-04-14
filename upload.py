import getserial
import db

dbd = [0]*3
dbd[0] = input('host : ')
dbd[1] = input('password : ')


while True:
    data = getserial.get()  # data[0] Ultra sonic sensor       data[1] Temperature sensor       data[2] Gyro sensor
    gyro = data[2].split('.')
    print(data[0] + '\t' + data[1] + '\t' + gyro[0] + ':' + gyro[1])
    if 0 == db.input(dbd, data):
        print("error")
    else:
        print("succes")