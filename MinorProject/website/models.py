from django.db import models

# Create your models here.
class Records(models.Model):
    OrderData = models.DateField()
    Name = models.CharField(max_length = 50)
    Email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    state = models.CharField(max_length = 50)
    producy = models.CharField(max_length = 100)
    quantity = models.IntegerField()
    unit = models.CharField(max_length = 10)