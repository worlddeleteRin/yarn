# Generated by Django 3.1.3 on 2021-01-31 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('imgsrc', models.ImageField(default='https://placehold.it/500x500', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('imgsrc', models.ImageField(default='https://placehold.it/500x500', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=None)),
                ('imgsrc', models.ImageField(default='https://placehold.it/500x500', upload_to='')),
                ('description', models.TextField()),
                ('code', models.CharField(max_length=200)),
                ('features', models.JSONField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.subcategory')),
            ],
        ),
    ]
