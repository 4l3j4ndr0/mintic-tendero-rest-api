# Generated by Django 4.1.1 on 2022-09-19 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_bussiness_table_alter_userbussiness_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('bar_code', models.CharField(max_length=25)),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sell_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('apply_iva', models.BooleanField(default=True)),
                ('send_alert', models.IntegerField()),
                ('bussiness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bussiness')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.provider')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('celphone', models.CharField(max_length=15)),
                ('bussiness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bussiness')),
            ],
            options={
                'db_table': 'customers',
            },
        ),
    ]
