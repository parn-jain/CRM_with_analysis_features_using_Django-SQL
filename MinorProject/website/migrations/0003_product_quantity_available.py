# Generated by Django 4.2.5 on 2023-11-21 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_product_remove_records_producy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity_available',
            field=models.IntegerField(default=0),
        ),
    ]
