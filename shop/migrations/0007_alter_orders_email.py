# Generated by Django 3.2.4 on 2021-07-06 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orders_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.CharField(max_length=111),
        ),
    ]