import getserial
import db

while True:
    data = getserial.get()
    print(data)
    # db.input('ULTRA', data[0])
    # db.input('GYRO', data[1])
    # db.input('TEMPERATURE', data[2])