# Generated by Django 3.2 on 2022-12-31 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='author_name',
            new_name='contact_name',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='author',
            new_name='contacter',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='Contactus_category',
            new_name='contactus_category',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='Contactus_description',
            new_name='contactus_description',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='Contactus_title',
            new_name='contactus_title',
        ),
    ]
