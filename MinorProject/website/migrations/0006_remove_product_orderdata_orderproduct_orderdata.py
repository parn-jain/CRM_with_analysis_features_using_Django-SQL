# Generated by Django 4.2.5 on 2023-11-21 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_remove_orderproduct_orderdata_product_orderdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='OrderData',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='OrderData',
            field=models.DateField(default='2023-01-01'),
        ),
    ]
