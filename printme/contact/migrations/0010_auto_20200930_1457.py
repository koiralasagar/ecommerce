# Generated by Django 3.0.2 on 2020-09-30 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_contact_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='product',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='product_id',
        ),
    ]
