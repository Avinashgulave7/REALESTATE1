# Generated by Django 3.1.2 on 2020-10-23 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0038_select_property_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='select_property',
            name='Agent',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='agent', to='testapp.agent'),
        ),
    ]
