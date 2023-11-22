# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Records, Product, OrderProduct
from .analysis import mean_qty
from .analysis import get_top_customer,generate_state_quantity_chart
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('data')
        else:
            messages.error(request, "There was an error")
            return redirect('home')
    else:
        context = {'variable': 'this was a variable'}
        return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def contactus(request):
    return render(request, "contact.html")

def services(request):
    return render(request, "services.html")

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

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
            quantity = int(request.POST[f'quantity{i + 1}'])
            unit = request.POST[f'unit{i + 1}']
            
            # Get or create the product instance
            product_instance, created = Product.objects.get_or_create(name=product_name)

            # Check if there is enough quantity available
            if product_instance.quantity_available >= quantity:
                # Create OrderProduct instance
                OrderProduct.objects.create(record=records_instance, product=product_instance, quantity=quantity, unit=unit)

                # Update the quantity_available field for the product
                product_instance.quantity_available -= quantity
                product_instance.save()

                # Add a success message
                messages.success(request, "Record has been added successfully")
            else:
                # Add an error message if there is not enough quantity available
                messages.error(request, f"Not enough quantity available for {product_name}")

        # Redirect to a success page or any other page as needed
        return redirect('home')  # Replace 'home' with the actual URL name

    # Retrieve products for displaying in the form
    products = Product.objects.all()
    return render(request, 'data.html', {'products': products})


def combined_view(request):
    # Call your analysis functions to get data
    result_mean_qty = mean_qty()
    result_top_customer = get_top_customer()


    # Generate the state vs quantity chart
    generate_state_quantity_chart()

    # Pass the data to the template
    context = {
        'result_mean_qty': result_mean_qty,
        'result_top_customer': result_top_customer,
        # 'chart_image_path': 'path/to/static/images/bar_chart.png',
        # 'state_quantity_chart_image_path': 'MinorProject\Static\images\state_quantity_chart.png',
    }

    # Render the HTML template
    return render(request, 'try.html', context)