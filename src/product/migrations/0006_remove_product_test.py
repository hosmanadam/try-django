# Generated by Django 2.0.7 on 2019-06-28 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='test',
        ),
    ]