# Generated by Django 4.2.2 on 2023-06-26 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dplants', '0008_product_price_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='prices',
            field=models.IntegerField(default=0),
        ),
    ]
