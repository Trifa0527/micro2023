import serial
import sqlite3

ser = serial.Serial("COM3", 115200, timeout = 1)
while True:
    print(ser.readline())