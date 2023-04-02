# Generated by Django 3.2 on 2022-12-31 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('share', '0004_auto_20221129_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_share', to=settings.AUTH_USER_MODEL),
        ),
    ]