from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method=='POST':
        email_id=request.POST['email']
        passwd=request.POST['password']
        auth=authenticate(email=email_id,password=passwd)
        if auth is None:
            return redirect('/')
            #messages.success(request, 'Incorrect Details')
            
        else:
            return redirect('/login')

    else:
        return render(request,'login.html')