# Generated by Django 3.1.2 on 2020-10-29 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_about_us_about_us_part'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about_us',
            options={'verbose_name_plural': 'About us'},
        ),
        migrations.AddField(
            model_name='about_us',
            name='image_alt',
            field=models.CharField(default='', max_length=255),
        ),
    ]
