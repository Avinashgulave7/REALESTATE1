# Generated by Django 3.1.2 on 2020-10-24 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0045_auto_20201024_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='Area',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
