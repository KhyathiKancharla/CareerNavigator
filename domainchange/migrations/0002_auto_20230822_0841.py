# Generated by Django 3.0.5 on 2023-08-22 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domainchange', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domain',
            name='links',
        ),
        migrations.AddField(
            model_name='domain',
            name='links',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='domain_link',
        ),
    ]