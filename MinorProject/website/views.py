from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authinticate
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request,"Threr was an error")
            return redirect('home')
    else:
        context = {'variable':'this was a variable'}
        return render(request, "index.html",context)
    # return HttpResponse("This is home page")

def about(request):
    return render(request, "about.html")

def contactus (request):
    return render(request, "contact.html")

def services (request):
    return render(request, "services.html")

def login_user(request):
    pass
def logout_user(request):
    logout(request)
    messages.success(request,"You have been loged out")
    return redirect('home')