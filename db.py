import pymysql

hostname = ''
username = ''
pw = ''
dbname = ''

def reset(table, sensor):
    # con = pymysql.connect(host=hostname, user=username, password=pw, db=dbname, charset='utf8')
    # cur = con.cursor()
    sql = 'DELETE FROM ' + table + '; ALTER TABLE ULTRA AUTO_INCREMENT = 1;'
    return 1

def input(table, data):
    # con = pymysql.connect(host=hostname, user=username, password=pw, db=dbname, charset='utf8')
    # cur = con.cursor()
    sqlinsdata = "INSERT INTO" + table + "(TIME, DATA) VALUES(NOW()," +  + data + ");"
    return 1