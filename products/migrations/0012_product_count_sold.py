# Generated by Django 3.1.6 on 2021-04-24 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20210407_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count_sold',
            field=models.IntegerField(default=0, verbose_name='count sold'),
        ),
    ]
