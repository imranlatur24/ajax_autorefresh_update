from django.shortcuts import render,HttpResponse
from .models import StudentModel
from django.http import JsonResponse
# Create your views here.

def dashboard(request):
    return render(request,"index.html")

def student_data(request):
    stud = StudentModel.objects.all()
    return JsonResponse({'students':list(stud.values())})

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
