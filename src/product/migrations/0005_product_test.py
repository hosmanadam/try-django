# Generated by Django 2.0.7 on 2019-06-28 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='test',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=20),
            preserve_default=False,
        ),
    ]