# Generated by Django 3.0.2 on 2020-09-29 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200929_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
