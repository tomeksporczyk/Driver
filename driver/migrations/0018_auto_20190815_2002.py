# Generated by Django 2.2.2 on 2019-08-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0017_auto_20190815_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='dislike',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
