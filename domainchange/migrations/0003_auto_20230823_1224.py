# Generated by Django 3.0.5 on 2023-08-23 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domainchange', '0002_auto_20230822_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]