# Generated by Django 3.1.2 on 2020-11-14 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20201112_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='drink_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.drink_type'),
        ),
    ]
