# Generated by Django 3.1.2 on 2020-10-18 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_signup'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='gallary',
            field=models.FileField(null=True, upload_to='img/', verbose_name=''),
        ),
    ]
