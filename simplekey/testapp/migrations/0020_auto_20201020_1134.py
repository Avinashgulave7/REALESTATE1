# Generated by Django 3.1.2 on 2020-10-20 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0019_buyimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyimage',
            name='buy',
        ),
        migrations.DeleteModel(
            name='Buy',
        ),
        migrations.DeleteModel(
            name='BuyImage',
        ),
    ]
