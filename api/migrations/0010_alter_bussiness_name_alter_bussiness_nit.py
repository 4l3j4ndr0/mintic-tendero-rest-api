# Generated by Django 4.1.1 on 2022-09-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_userbussiness_bussiness_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bussiness',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='bussiness',
            name='nit',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]