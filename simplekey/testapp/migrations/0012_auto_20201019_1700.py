# Generated by Django 3.1.2 on 2020-10-19 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0011_buyimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimage',
            name='post',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='user',
        ),
        migrations.RemoveField(
            model_name='buy',
            name='gallary',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
    ]
