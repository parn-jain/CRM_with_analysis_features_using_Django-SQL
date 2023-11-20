import os
import sys
import django
sys.path.append("D:/College/5th Sem/Minor Project/MinorProject")  # Replace with the correct path to your project root
os.environ['DJANGO_SETTINGS_MODULE'] = 'MinorProject.settings'

from django.db import connection

def fetch_records():
    with connection.cursor() as cursor:
        # Execute a raw SQL query to fetch records data
        cursor.execute("SELECT * FROM website_records")
        
        # Fetch all rows from the result set
        records = cursor.fetchall()
        print(type(records))
        # print(records)

        # Process the records data
        for record in records:
            print(record)

def fetch_products():
    with connection.cursor() as cursor:
        # Execute a raw SQL query to fetch products data
        cursor.execute("SELECT * FROM website_product")
        
        # Fetch all rows from the result set
        products = cursor.fetchall()

        # Process the products data
        for product in products:
            print(product)

def fetch_order_products():
    with connection.cursor() as cursor:
        # Execute a raw SQL query to fetch order products data
        cursor.execute("SELECT * FROM website_orderproduct")
        
        # Fetch all rows from the result set
        order_products = cursor.fetchall()

        # Process the order products data
        for order_product in order_products:
            print(order_product)

# Example usage
fetch_records()
# fetch_products()
# fetch_order_products()
