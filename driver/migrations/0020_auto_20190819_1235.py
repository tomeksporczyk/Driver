# Generated by Django 2.2.2 on 2019-08-19 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0019_auto_20190816_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='driver.TestQuestion'),
        ),
    ]