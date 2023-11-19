import os
import sys
import django
sys.path.append("D:/College/5th Sem/Minor Project/MinorProject")  # Replace with the correct path to your project root
os.environ['DJANGO_SETTINGS_MODULE'] = 'MinorProject.settings'

# Initialize Django
django.setup()

from models import Records, Product, OrderProduct


from django.db import models
# from django.contrib import admin
from models import Records, Product, OrderProduct

# Example 1: Retrieve all records
all_records = Records.objects.all()

# Example 2: Retrieve a specific record by ID
record_id = 1
specific_record = Records.objects.get(id=record_id)

# Example 3: Retrieve all products
all_products = Product.objects.all()

# Example 4: Retrieve a specific product by ID
product_id = 1
specific_product = Product.objects.get(id=product_id)

# Example 5: Retrieve all order products
all_order_products = OrderProduct.objects.all()

# Example 6: Retrieve order products associated with a specific record
record_order_products = specific_record.orderproduct_set.all()

# Example 7: Perform some calculations (e.g., total quantity of a specific product)
total_quantity_product_id = 1
total_quantity = OrderProduct.objects.filter(product_id=total_quantity_product_id).aggregate(total_quantity=models.Sum('quantity'))

# Example 8: Perform calculations involving related models (e.g., total quantity of all products for a specific record)
total_quantity_for_record = specific_record.orderproduct_set.aggregate(total_quantity=models.Sum('quantity'))

# You can now use the retrieved data and perform any necessary calculations or analysis in your Python code.
# For example, you can iterate through the records, products, or order products and apply your logic.

# Example 9: Iterate through all records and print their names and associated order products
for record in all_records:
    print(f"Record: {record.Name}")
    for order_product in record.orderproduct_set.all():
        print(f"  Product: {order_product.product.name}, Quantity: {order_product.quantity}")

# Note: Adjust the app name ('yourapp') according to your actual Django app name.
