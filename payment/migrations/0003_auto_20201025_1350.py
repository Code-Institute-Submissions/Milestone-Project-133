# Generated by Django 3.1.2 on 2020-10-25 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20201025_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drinkorderlineitem',
            old_name='drink',
            new_name='drink_name',
        ),
    ]
