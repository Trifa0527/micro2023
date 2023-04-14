from django.http import JsonResponse
from django.shortcuts import render
import random
import pymysql

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')

def update(request):
    con = pymysql.connect(host='', user='yys', password='', db='micro', charset='utf8')
    cur = con.cursor(pymysql.cursors.DictCursor)
    sql = '''SELECT * FROM DATA ORDER BY orders DESC LIMIT 1;'''
    cur.execute(sql)
    data = cur.fetchone()
    con.close()
    gyro = data['gyro'].split('.')
    a = {'time' : data['times'], 'ult' : data['ult'], 'tem' : data['temp'], 'gyro_x' : gyro[0], 'gyro_y' : gyro[1]}
    return JsonResponse(a)