# Generated by Django 4.2.5 on 2023-11-21 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_records_orderdata_orderproduct_orderdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='OrderData',
        ),
        migrations.AddField(
            model_name='product',
            name='OrderData',
            field=models.DateField(default='2023-01-01'),
        ),
    ]