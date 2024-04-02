from django.shortcuts import render 
from django.http import HttpResponse
from .forms import UserForm

a=[]

def index(request):                                        
    if request.method == "POST":
        userform=UserForm(request.POST)     
        name = request.POST.get("name")
        age = request.POST.get("age")
        password = request.POST.get("password")           # Берем все значения, которые передали в формы 
        a.append(name)
        return render(request, "main.html",{"name":name})       # Отправляем их на страницы about/  
    else:     
        userform = UserForm()      
        return render(request, "index.html", {"form": userform})
    
    
def main(request):
    name=request.POST.get('name')
    return render(request,"main.html",{'name':name})



