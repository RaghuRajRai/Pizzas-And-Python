# Generated by Django 2.2 on 2019-04-26 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20190426_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]