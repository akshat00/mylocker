# Generated by Django 3.0.2 on 2020-01-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupmodel',
            name='username',
            field=models.CharField(default='abc', max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
