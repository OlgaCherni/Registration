from django.shortcuts import render 
from django.http import HttpResponse
from pril.views import a                     
from datetime import datetime # Дата/время


# Create your views here.

def about(request):
    name=a[0]
    age=25    
    return render(request, 'about.html',{'name':name,"age":age})


def time(request):
    date= datetime.now()        # Дата/время
    return render(request, 'date.html',{"date":date})  