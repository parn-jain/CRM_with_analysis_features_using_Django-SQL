from django.contrib import admin
from .models import Records

# admin.site.register(Records)
# Register your models here.
from django.contrib import admin
from .models import Records, Product, OrderProduct

from django.contrib import admin
from .models import Records, Product, OrderProduct

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

class RecordsAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]
    list_display = ('id', 'OrderData', 'Name', 'Email', 'phone', 'city', 'address', 'state')

class ProductAdmin(admin.ModelAdmin):
     list_display = ('id', 'name')
    # pass

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'record', 'product', 'quantity', 'unit')

admin.site.register(Records, RecordsAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)

