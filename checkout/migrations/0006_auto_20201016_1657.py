# Generated by Django 3.1.2 on 2020-10-16 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20201016_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drinkorder',
            name='order_total',
        ),
        migrations.AlterField(
            model_name='drinkorder',
            name='postcode',
            field=models.CharField(max_length=20, null=True),
        ),
    ]