from django.shortcuts import render
from scanner.models import Register,Login
from qrcode import*
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
#from django.shortcuts import  render, redirect
#from .forms import NewUserForm
#from django.contrib.auth import login
#from django.contrib import messages

def register_request(request):
    if request.method=="POST":
        vehicle = request.POST['vehicle']
        password = request.POST['password']
        phone = request.POST['phone']
        email = request.POST['email']

        ins = Register(vehicle=vehicle, password=password, phone=phone, email=email)
        ins.save()

        print("data has been written to database")
    return render(request, 'register.html')
          
        
def login(request):
    if request.method=="POST":
        vehicle = request.POST['vehicle']
        password = request.POST['password']

        all_members=Register.objects.filter(vehicle=vehicle,password=password).values()
        if all_members.exists():
            return render(request, 'profile.html',{'all':all_members})
        else:  
            print(all_members)
            return render(request, 'error.html')
    print("data has been written to database")
    return render(request, 'login.html')


def scanner_function(request):
    global data
    if request.method == "POST":
        data = request.POST['data']

        img = make(data)
        img.save('scanner\static\img\img1.jpg')
    else:
        pass

    return render(request, 'scanner1.html',{'data':data})



        
        

    