# Generated by Django 3.0.2 on 2020-01-12 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=16)),
                ('last_name', models.CharField(max_length=16)),
                ('email_address', models.EmailField(max_length=256, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('phone_number', models.BigIntegerField()),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
