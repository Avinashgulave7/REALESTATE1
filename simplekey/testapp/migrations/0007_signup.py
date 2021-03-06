# Generated by Django 3.1.2 on 2020-10-16 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import testapp.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0006_agent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, validators=[testapp.validators.validate_username_length, testapp.validators.validate_username_alphadigits], verbose_name='User name')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('password1', models.CharField(max_length=30, validators=[testapp.validators.validate_password_length, testapp.validators.validate_password_digit, testapp.validators.validate_password_uppercase])),
                ('password2', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=15, validators=[testapp.validators.validate_phonenumber])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
