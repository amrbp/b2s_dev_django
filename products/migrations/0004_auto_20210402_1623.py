# Generated by Django 3.1.6 on 2021-04-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210402_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(max_length=20),
        ),
    ]