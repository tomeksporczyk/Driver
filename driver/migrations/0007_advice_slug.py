# Generated by Django 2.2.2 on 2019-07-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0006_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='advice',
            name='slug',
            field=models.SlugField(default='test'),
            preserve_default=False,
        ),
    ]