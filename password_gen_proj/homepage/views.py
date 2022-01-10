from django.http import HttpResponse
from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request,template_name='home.html')


def gen_password(request):
    genpass=''
    password=list('abcdefghijklmnopqrstuvwxyz0123456789')
    if request.GET.get('uppercase')=='on':
        password.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers')=='on':
        password.extend(list('0123456789'))
    if request.GET.get('special') == 'on':
        password.extend(list('!@#$&+%*)('))

    for i in range(int(request.GET.get('length',12))):
        genpass+=random.choice(password)


    return render(request,template_name='password.html' ,context={'password':genpass})