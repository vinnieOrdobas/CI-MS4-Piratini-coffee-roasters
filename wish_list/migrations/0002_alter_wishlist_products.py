# Generated by Django 3.2.6 on 2021-09-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('wish_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='products',
            field=models.ManyToManyField(related_name='products', to='products.Product'),
        ),
    ]