# Generated by Django 4.2.7 on 2023-11-23 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_cartmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='product_image',
            field=models.ImageField(upload_to='products'),
        ),
    ]
