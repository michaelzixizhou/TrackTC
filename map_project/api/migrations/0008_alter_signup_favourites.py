# Generated by Django 4.1.3 on 2022-11-06 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_signup_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='favourites',
            field=models.CharField(default='', max_length=500),
        ),
    ]