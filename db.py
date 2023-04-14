import pymysql

def reset(db):
    # con = pymysql.connect(host=db[0], user=db[1], password=db[2], db=dbname, charset='utf8')
    # cur = con.cursor()
    sql = 'DELETE FROM DATA; ALTER TABLE ULTRA AUTO_INCREMENT = 1;'
    return 1

def input(db, data): # data[0] Ultra sonic sensor       data[1] Temperature sensor       data[2] Gyro sensor
    sql = "INSERT INTO DATA(times, ult, temp, gyro) VALUES(NOW()," + data[0] + ',' + data[1] + ',' + data[2] + ");"
    con = pymysql.connect(host=db[0], user='yys', password=db[1], db='micro', charset='utf8')
    cur = con.cursor(pymysql.cursors.DictCursor)
    a = cur.execute(sql)
    con.commit()
    con.close()
    return a