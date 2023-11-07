from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Records


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
            return redirect('data')
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

# def data (request):
#     return render(request, "data.html")



def data(request):
    if request.method == 'POST':
        # Extract form data from request.POST dictionary
        order_data = request.POST.get('OrderData')
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        address = request.POST.get('address')
        state = request.POST.get('state')
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        unit = request.POST.get('unit')

        # create a function here which convert comma seperated data to a list 

        # Create a new Records object and save it to the database
        record = Records(
            OrderData=order_data,
            Name=name,
            Email=email,
            phone=phone,
            city=city,
            address=address,
            state=state,
            producy=product,
            quantity=quantity,
            unit=unit
        )
        record.save()

        # Add a success message
        messages.success(request, "Record has been added successfully")

        # Redirect to a success page or any other page as needed
        return redirect('home')  # Replace 'success_page' with the actual URL name

    # Render the form template for GET requests
    return render(request, 'data.html')