# Generated by Django 3.1.3 on 2021-02-01 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_product_sale_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
