# Generated by Django 3.0.2 on 2021-02-24 02:18

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210224_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(validators=[product.models.minpricevalidator]),
        ),
    ]