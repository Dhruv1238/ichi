from sugoi.models import Form
from django.shortcuts import render, HttpResponse
from sugoi.models import Form

# Create your views here.

def index(request):
   return render(request , 'index.html')

def home(request):
     return render(request , 'home.html')

def contact(request):
    return render(request , 'contact.html')
   
def form(request):
    
    return render(request , 'form.html')   

def submitted(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        query =request.POST.get('query')
        phone =request.POST.get('phone')
        form = Form(name=name, email=email, query=query, phone=phone,)
        form.save()
    return render(request, 'submitted.html')

def history(request):
    return render(request, 'history.html')
        

    #return HttpResponse("Hite desu")