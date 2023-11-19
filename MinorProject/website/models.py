# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=100)

# class Records(models.Model):
#     OrderData = models.DateField()
#     Name = models.CharField(max_length=50)
#     Email = models.EmailField(max_length=100)
#     phone = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     address = models.CharField(max_length=100)
#     state = models.CharField(max_length=50)
#     products = models.ManyToManyField(Product, through='OrderProduct')
    
# class OrderProduct(models.Model):
#     record = models.ForeignKey(Records, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     unit = models.CharField(max_length=10)



from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Records(models.Model):
    OrderData = models.DateField()
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    products = models.ManyToManyField(Product, through='OrderProduct')

    def __str__(self):
        return self.Name  # Display the customer's name in the admin

class OrderProduct(models.Model):
    record = models.ForeignKey(Records, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.record.Name} - {self.product.name}"  # Display customer's name and product's name in the admin