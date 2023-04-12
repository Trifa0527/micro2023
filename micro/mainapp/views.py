from django.http import JsonResponse
from django.shortcuts import render
import random
from . import getserial

# Create your views here.
def index(request):
    a = {'a' : random.randrange(0, 101), 'b' : ''}
    if a['a'] > 50:
        a['b'] = '<img src="https://img.segye.com/content/image/2021/05/16/20210516505887.jpg">'
    else:
        a['b'] = '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Elon_Musk_Royal_Society.jpg/225px-Elon_Musk_Royal_Society.jpg">'
    return render(request, 'mainapp/index.html', a)

def update(request):
    # da = getserial.get()
    da = [random.randrange(0,100), random.randrange(0,100), random.randrange(0,100)]
    a = {'ult' : da[0], 'tem' : da[1], 'gyro' : da[2]}
    return JsonResponse(a)