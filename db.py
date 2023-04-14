import pymysql

def reset(db):
    con = pymysql.connect(host=db[0], user='yys', password=db[1], db='micro', charset='utf8')
    cur = con.cursor()
    sql = '''DELETE FROM DATA;'''
    sqldel = '''ALTER TABLE DATA AUTO_INCREMENT = 1;'''
    cur.execute(sql)
    cur.execute(sqldel)
    a = con.commit()
    con.close()
    return a

def input(db, data): # data[0] Ultra sonic sensor       data[1] Temperature sensor       data[2] Gyro sensor
    sql = "INSERT INTO DATA(times, ult, temp, gyro) VALUES(NOW()," + data[0] + ',' + data[1] + ',' + data[2] + ");"
    con = pymysql.connect(host=db[0], user='yys', password=db[1], db='micro', charset='utf8')
    cur = con.cursor(pymysql.cursors.DictCursor)
    cur.execute(sql)
    a = con.commit()
    con.close()
    return a