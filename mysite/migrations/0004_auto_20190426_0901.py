# Generated by Django 2.2 on 2019-04-26 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_cart_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='password',
        ),
        migrations.AlterField(
            model_name='orders',
            name='cart',
            field=models.CharField(max_length=500),
        ),
    ]
