import os
import sys
import django
sys.path.append("D:/College/5th Sem/Minor Project/MinorProject")  # Replace with the correct path to your project root
os.environ['DJANGO_SETTINGS_MODULE'] = 'MinorProject.settings'

from django.db import connection
import matplotlib.pyplot as plt
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


def qty():
    with connection.cursor() as cursor:
        # Execute a raw SQL query to fetch order products data
        cursor.execute("SELECT * FROM website_orderproduct")
        
        # Fetch all rows from the result set
        order_products = cursor.fetchall()

        # Process the order products data
        qty = []
        for order_qty in order_products:
            qty.append(order_qty[1])
        print(qty)   
        return qty
def generate_bar_chart():
    with connection.cursor() as cursor:
        cursor.execute("SELECT category, COUNT(*) FROM website_records GROUP BY category")
        data = cursor.fetchall()

        categories, counts = zip(*data)

        # Create a bar chart using Matplotlib
        plt.bar(categories, counts)
        plt.xlabel('Category')
        plt.ylabel('Count')
        plt.title('Record Count by Category')
        plt.savefig('path/to/static/images/bar_chart.png')
def mean_qty():
    print(sum(qty()))
    return sum(qty())
mean_qty()


from django.db import connection

def get_top_customer():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                r.id as customer_id,
                r.Name as customer_name,
                SUM(op.quantity) as total_quantity
            FROM
                website_records r
            JOIN
                website_orderproduct op ON r.id = op.record_id
            GROUP BY
                r.id, r.Name
            ORDER BY
                total_quantity DESC
            LIMIT 1;
        """)
        top_customer = cursor.fetchone()

    if top_customer:
        top_customer_dict = {
            'customer_id': top_customer[0],
            'customer_name': top_customer[1],
            'total_quantity': top_customer[2],
        }
        return top_customer_dict
    else:
        return None

# Example usage
# top_customer = get_top_customer()
# if top_customer:
#     print(f"Top Customer: {top_customer['customer_name']} (ID: {top_customer['customer_id']}) with total quantity {top_customer['total_quantity']}")
# else:
#     print("No top customer found.")


# import matplotlib.pyplot as plt

