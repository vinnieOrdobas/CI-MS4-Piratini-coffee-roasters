# Generated by Django 3.2.6 on 2021-09-15 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210915_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_membership',
        ),
    ]