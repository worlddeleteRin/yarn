# Generated by Django 3.0.8 on 2020-10-21 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='pr_id',
            field=models.IntegerField(default=0),
        ),
    ]
