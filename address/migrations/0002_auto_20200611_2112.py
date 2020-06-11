# Generated by Django 3.0.3 on 2020-06-11 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='address',
            name='district',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='address',
            name='hnumber',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
