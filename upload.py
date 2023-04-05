import serial
import pymysql

ser = serial.Serial("COM3", 115200, timeout = 1)
con = pymysql.connect(host='localhost', user='mysql_user_id', password='_password_', db='Data', charset='utf8')

cur = con.cursor()

data = None
order = None
sqlinsdata = "INSERT INTO A VALUES(NOW(), " + order + ", " + data + ");"
while True:
    if ser.readable():
        orgdata = ser.readline()
        