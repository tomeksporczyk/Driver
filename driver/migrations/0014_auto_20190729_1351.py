# Generated by Django 2.2.2 on 2019-07-29 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0013_testanswer_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
