# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity_available = models.IntegerField(default=0)  # Added field for quantity available

    def __str__(self):
        return self.name

class Records(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    products = models.ManyToManyField(Product, through='OrderProduct')

    def __str__(self):
        return self.Name

class OrderProduct(models.Model):
    OrderData = models.DateField(default='2023-01-01')  # Moved the OrderData field here
    record = models.ForeignKey(Records, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.record.Name} - {self.product.name}"


# # signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# @receiver(post_save, sender=OrderProduct)
# def update_quantity_available(sender, instance, **kwargs):
#     # Update the quantity_available field when an order is placed
#     product = instance.product
#     product.quantity_available -= instance.quantity
#     product.save()
