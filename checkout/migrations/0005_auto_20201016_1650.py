# Generated by Django 3.1.2 on 2020-10-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_drinkorder_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinkorder',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]