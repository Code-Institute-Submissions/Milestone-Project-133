# Generated by Django 3.1.2 on 2020-10-30 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20201030_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_us',
            name='image_description',
            field=models.CharField(default='', max_length=255),
        ),
    ]
