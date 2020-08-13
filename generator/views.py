from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    #return render(request,'generator/home.html',{'password':'hshhshhs'})
    return render(request,'generator/home.html')
def about(request):
    return render(request,'generator/about.html')
   # return HttpResponse("<h1>hello This is Home page</h1>")
def password(request):
    #thispassword='testing'
    characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    length=int(request.GET.get('length',12))
    thispassword=''
    for x in range(length):
        thispassword+=random.choice(characters)

    return render(request,'generator/password.html',{'password':thispassword})