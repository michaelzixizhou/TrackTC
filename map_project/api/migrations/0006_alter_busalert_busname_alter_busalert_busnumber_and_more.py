
# Generated by Django 4.1.3 on 2022-11-06 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_busalert_busname_alter_busalert_busnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busalert',
            name='busname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='busalert',
            name='busnumber',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
