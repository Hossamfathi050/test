# Generated by Django 4.1.7 on 2023-03-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='skills_category',
            field=models.CharField(choices=[('انتاج ونصميم المقررات الإلكترونية', 'انتاج ونصميم المقررات الإلكترونية'), ('التقويم الإلكتروني عن بعد', 'التقويم الإلكتروني عن بعد'), ('إدارة الفصول الإفتراضية', 'إدارة الفصول الإفتراضية'), ('تطبيقات الحوسبة السحابية', 'تطبيقات الحوسبة السحابية')], max_length=50),
        ),
    ]
