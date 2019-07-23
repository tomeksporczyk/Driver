# Generated by Django 2.2.2 on 2019-07-23 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advice',
            name='media',
            field=models.FileField(upload_to='advice/'),
        ),
        migrations.AlterField(
            model_name='forumtopic',
            name='name',
            field=models.CharField(max_length=512, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]