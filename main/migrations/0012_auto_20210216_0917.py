# Generated by Django 3.1.3 on 2021-02-16 09:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210207_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 16, 9, 17, 26, 378751, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 16, 9, 17, 26, 378784, tzinfo=utc)),
        ),
    ]
