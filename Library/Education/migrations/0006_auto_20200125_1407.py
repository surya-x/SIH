# Generated by Django 3.0.1 on 2020-01-25 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0005_auto_20200124_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
