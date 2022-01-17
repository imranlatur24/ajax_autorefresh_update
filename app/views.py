from django.shortcuts import render,HttpResponse
from .models import StudentModel,Listdata
from django.http import JsonResponse
# Create your views here.

def dashboard(request):
    return render(request,"index.html")

def getProducts(request):
    products = Listdata.objects.all()
    return JsonResponse({'products':list(products.values())})

def create(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobiles=request.POST['mobiles']
        print(name)
        print(email)
        print(mobiles)
        std = StudentModel(name=name,email=email,mobiles=mobiles)
        std.save()
        return HttpResponse('data submitted successfully')
