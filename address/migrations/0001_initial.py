# Generated by Django 3.0.3 on 2020-06-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hnumber', models.CharField(max_length=20)),
                ('locality', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('pincode', models.IntegerField(max_length=6)),
            ],
        ),
    ]
