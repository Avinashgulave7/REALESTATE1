# Generated by Django 3.1.2 on 2020-10-23 12:39

from django.db import migrations, models
import testapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0040_auto_20201023_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy',
            name='Area',
        ),
        migrations.AlterField(
            model_name='buy',
            name='Contact',
            field=models.IntegerField(validators=[testapp.validators.validate_phonenumber]),
        ),
        migrations.AlterField(
            model_name='buy',
            name='Price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='buy',
            name='Property',
            field=models.CharField(choices=[('', 'Select'), ('residential', 'Residential'), ('commercial', 'commercial')], default='select', max_length=20),
        ),
        migrations.AlterField(
            model_name='land',
            name='Area',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='land',
            name='Contact',
            field=models.IntegerField(validators=[testapp.validators.validate_phonenumber]),
        ),
        migrations.AlterField(
            model_name='land',
            name='Price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rent',
            name='Area',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rent',
            name='Contact',
            field=models.IntegerField(validators=[testapp.validators.validate_phonenumber]),
        ),
        migrations.AlterField(
            model_name='rent',
            name='Price',
            field=models.IntegerField(),
        ),
    ]
