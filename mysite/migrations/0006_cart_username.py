# Generated by Django 2.2 on 2019-04-26 03:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20190426_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]