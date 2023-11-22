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





# GRAPH
# Import necessary libraries
import matplotlib.pyplot as plt
from django.db import connection

# Import necessary libraries
import matplotlib.pyplot as plt
from django.db import connection

def fetch_state_quantity():
    with connection.cursor() as cursor:
        # Execute a raw SQL query to fetch state and quantity data
        cursor.execute("""
            SELECT
                r.state,
                SUM(op.quantity) as total_quantity
            FROM
                website_records r
            JOIN
                website_orderproduct op ON r.id = op.record_id
            GROUP BY
                r.state
        """)
        data = cursor.fetchall()

        states, quantities = zip(*data)

        return states, quantities

def generate_state_quantity_chart():
    states, quantities = fetch_state_quantity()

    # Create a new figure and axes
    fig, ax = plt.subplots()

    # Create a bar chart using Matplotlib
    ax.bar(states, quantities)
    ax.set_xlabel('State')
    ax.set_ylabel('Total Quantity')
    ax.set_title('State vs Quantity')

    # Save the figure with a unique name
    # fig.savefig('path/to/static/images/state_quantity_chart.png')
    fig.savefig('Static/images/state_quantity_chart.png')



def fetch_city_quantity():
    with connection.cursor() as cursor:
        # Execute a raw SQL query to fetch city and quantity data
        cursor.execute("""
            SELECT
                r.city,
                SUM(op.quantity) as total_quantity
            FROM
                website_records r
            JOIN
                website_orderproduct op ON r.id = op.record_id
            GROUP BY
                r.city
        """)
        data = cursor.fetchall()

        cities, quantities = zip(*data)

        return cities, quantities

def generate_city_quantity_chart():
    cities, quantities = fetch_city_quantity()

    # Create a new figure and axes
    fig, ax = plt.subplots()

    # Create a bar chart using Matplotlib
    ax.bar(cities, quantities, color = 'red')
    ax.set_xlabel('City')
    ax.set_ylabel('Total Quantity')
    ax.set_title('City vs Quantity')

    # Save the figure with a unique name
    # fig.savefig('path/to/static/images/city_quantity_chart.png')
    fig.savefig('Static/images/city_quantity_chart.png')







def fetch_date_quantity():
    with connection.cursor() as cursor:
        # Execute a raw SQL query to fetch date and quantity data
        cursor.execute("""
            SELECT
                op.OrderData,
                SUM(op.quantity) as total_quantity
            FROM
                website_orderproduct op
            GROUP BY
                op.OrderData
        """)
        data = cursor.fetchall()

        dates, quantities = zip(*data)

        return dates, quantities

def generate_date_quantity_chart():
    dates, quantities = fetch_date_quantity()

    # Create a new figure and axes
    fig, ax = plt.subplots()

    # Create a bar chart using Matplotlib
    # ax.bar(dates, quantities)
    ax.plot(dates, quantities, marker='o', linestyle='-', color='b', label='Total Quantity')
    ax.set_xlabel('Date')
    ax.set_ylabel('Total Quantity')
    ax.set_title('Date vs Quantity')

    # Save the figure with a unique name
    # fig.savefig('path/to/static/images/date_quantity_chart.png')
    plt.savefig('Static/images/date_quantity_chart.png')




    # plt.savefig('Static/images/city_quantity_chart.png')




def get_top_product():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                p.id as product_id,
                p.name as product_name,
                SUM(op.quantity) as total_quantity
            FROM
                website_product p
            JOIN
                website_orderproduct op ON p.id = op.product_id
            GROUP BY
                p.id, p.name
            ORDER BY
                total_quantity DESC
            LIMIT 1;
        """)
        top_product = cursor.fetchone()

    if top_product:
        top_product_dict = {
            'product_id': top_product[0],
            'product_name': top_product[1],
            'total_quantity': top_product[2],
        }
        return top_product_dict
    else:
        return None
    
def fetch_product_quantities():
    with connection.cursor() as cursor:
        # Execute a raw SQL query to fetch product and quantity data
        cursor.execute("""
            SELECT
                p.name,
                SUM(op.quantity) as total_quantity
            FROM
                website_product p
            JOIN
                website_orderproduct op ON p.id = op.product_id
            GROUP BY
                p.name
        """)
        data = cursor.fetchall()

        product_names, quantities = zip(*data)

        return product_names, quantities

def generate_product_quantity_pie_chart():
    product_names, quantities = fetch_product_quantities()

    # Create a new figure and axes
    fig, ax = plt.subplots()

    # Create a pie chart using Matplotlib
    ax.pie(quantities, labels=product_names, autopct='%1.1f%%', startangle=90)

    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis('equal')  

    # Set the title
    ax.set_title('Product Quantity Distribution')

    # Save the figure with a unique name
    plt.savefig('Static/images/product_quantity_pie_chart.png')
