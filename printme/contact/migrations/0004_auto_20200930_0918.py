# Generated by Django 3.0.2 on 2020-09-30 03:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20200929_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='product',
            field=models.CharField(default="All Product",max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
    ]