# Generated by Django 3.1.2 on 2020-10-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20201015_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Owner_name', models.CharField(max_length=20)),
                ('Contact', models.IntegerField()),
                ('Property_name', models.CharField(max_length=40)),
                ('Property', models.CharField(choices=[('residential', 'Residential'), ('commercial', 'commercial')], default='residential', max_length=20)),
                ('Type', models.CharField(choices=[('flat', 'Flat'), ('bunglow', 'Bunglow'), ('shop', 'Shop'), ('office', 'Office')], default='flat', max_length=20)),
                ('Rooms', models.IntegerField()),
                ('Baths', models.IntegerField()),
                ('Area', models.FloatField()),
                ('Water', models.CharField(choices=[('24/7', '24/7'), ('morning', 'Morning'), ('night', 'Night')], default='24/7', max_length=20)),
                ('Playground', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('in_future', 'In_Future')], default='yes', max_length=20)),
                ('Price', models.FloatField()),
                ('Description', models.TextField()),
                ('Gym', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('in_future', 'In_Future')], default='yes', max_length=20)),
                ('Hospital', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('in_future', 'In_Future')], default='yes', max_length=20)),
                ('School', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('in_future', 'In_Future')], default='yes', max_length=20)),
                ('Mall', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('in_future', 'In_Future')], default='yes', max_length=20)),
                ('Pincode', models.IntegerField()),
                ('State', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=20)),
                ('Address', models.TextField()),
                ('Img1', models.ImageField(upload_to='img/')),
                ('Electricity', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=20)),
                ('Parking', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('in_future', 'In_Future')], default='yes', max_length=20)),
                ('Club', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('in_future', 'In_Future')], default='yes', max_length=20)),
                ('Fire', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('in_future', 'In_Future')], default='yes', max_length=20)),
                ('Lift', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=20)),
                ('Wifi', models.CharField(choices=[('24/7', '24/7'), ('morning', 'Morning'), ('night', 'Night')], default='yes', max_length=20)),
                ('Security', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('in_future', 'In_Future')], default='yes', max_length=20)),
                ('Temple', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('in_future', 'In_Future')], default='yes', max_length=20)),
                ('Poll', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('in_future', 'In_Future')], default='yes', max_length=20)),
                ('Living', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('in_future', 'In_Future')], default='yes', max_length=20)),
                ('Hotel', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('in_future', 'In_Future')], default='yes', max_length=20)),
                ('Cinema', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('in_future', 'In_Future')], default='yes', max_length=20)),
                ('Date', models.DateField()),
            ],
        ),
    ]