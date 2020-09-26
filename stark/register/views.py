from django.shortcuts import render,redirect
from django.contrib.auth.models import User 



# Create your views here.
def register (request):
    if request.method=='POST':
       username=request.POST['name']
       email_id=request.POST['email']
       passwd=request.POST['password']
       x=User.objects.create_user(username=username,email=email_id,password=passwd)
       x.save()
       return redirect('/')
       

    else:
        return render(request,'register.html')