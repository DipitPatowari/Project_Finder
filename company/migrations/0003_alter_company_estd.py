# Generated by Django 4.2.1 on 2023-06-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='estd',
            field=models.PositiveIntegerField(blank=True, max_length=100, null=True),
        ),
    ]
