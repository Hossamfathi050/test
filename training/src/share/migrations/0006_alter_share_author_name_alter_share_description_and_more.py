# Generated by Django 4.1.7 on 2023-03-27 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0005_alter_share_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='author_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='share',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='share',
            name='share_category',
            field=models.CharField(choices=[('انتاج ونصميم المقررات الإلكترونية', 'انتاج ونصميم المقررات الإلكترونية'), ('التقويم الإلكتروني عن بعد', 'التقويم الإلكتروني عن بعد'), ('إدارة الفصول الإفتراضية', 'إدارة الفصول الإفتراضية'), ('تطبيقات الحوسبة السحابية', 'تطبيقات الحوسبة السحابية')], max_length=50),
        ),
        migrations.AlterField(
            model_name='share',
            name='share_title',
            field=models.CharField(max_length=50),
        ),
    ]
