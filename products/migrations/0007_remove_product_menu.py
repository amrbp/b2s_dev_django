# Generated by Django 3.1.6 on 2021-04-02 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210402_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='menu',
        ),
    ]
