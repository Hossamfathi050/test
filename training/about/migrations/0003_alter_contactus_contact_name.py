# Generated by Django 3.2 on 2022-12-31 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20221231_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='contact_name',
            field=models.CharField(max_length=15, verbose_name='اسم المرسل'),
        ),
    ]
