import getserial
import micro.mainapp.db as db

db[0] = input('host : ')
db[1] = input('user : ')
db[2] = input('password : ')

while True:
    data = getserial.get()  # data[0] Ultra sonic sensor       data[1] Temperature sensor       data[2] Gyro sensor
    print(data)
    # db.input(db, data)