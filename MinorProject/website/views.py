from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Records, Product, OrderProduct


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



# def data(request):
#     if request.method == 'POST':
#         # Extract form data from request.POST dictionary
#         order_data = request.POST.get('OrderData')
#         name = request.POST.get('Name')
#         email = request.POST.get('Email')
#         phone = request.POST.get('phone')
#         city = request.POST.get('city')
#         address = request.POST.get('address')
#         state = request.POST.get('state')
#         product = request.POST.get('product')
#         quantity = request.POST.get('quantity')
#         unit = request.POST.get('unit')

#         # create a function here which convert comma seperated data to a list 

#         # Create a new Records object and save it to the database
#         record = Records(
#             OrderData=order_data,
#             Name=name,
#             Email=email,
#             phone=phone,
#             city=city,
#             address=address,
#             state=state,
#             producy=product,
#             quantity=quantity,
#             unit=unit
#         )
#         record.save()

#         # Add a success message
#         messages.success(request, "Record has been added successfully")

#         # Redirect to a success page or any other page as needed
#         return redirect('home')  # Replace 'success_page' with the actual URL name

#     # Render the form template for GET requests
#     return render(request, 'data.html')



def data(request):
    if request.method == 'POST':
        # Retrieve customer details from the form
        order_date = request.POST['OrderData']
        name = request.POST['Name']
        email = request.POST['Email']
        phone = request.POST['phone']
        city = request.POST['city']
        address = request.POST['address']
        state = request.POST['state']

        # Create Records instance
        records_instance = Records.objects.create(
            OrderData=order_date,
            Name=name,
            Email=email,
            phone=phone,
            city=city,
            address=address,
            state=state
        )

        # Retrieve and create products associated with the customer
        product_fields = [request.POST[f'product{i}'] for i in range(1, len(request.POST) + 1) if f'product{i}' in request.POST]
        for i in range(len(product_fields)):
            product_name = request.POST[f'product{i + 1}']
            quantity = int(request.POST[f'quantity{i + 1}'])  # Assuming corresponding quantity fields are named as quantity1, quantity2, ...
            unit = request.POST[f'unit{i + 1}']  # Assuming corresponding unit fields are named as unit1, unit2, ...
            product_instance, created = Product.objects.get_or_create(name=product_name)
            OrderProduct.objects.create(record=records_instance, product=product_instance, quantity=quantity, unit=unit)

        # Handle the rest of your logic (e.g., redirecting to a success page)
        # ...

    return render(request, 'data.html')
