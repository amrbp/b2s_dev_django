# Generated by Django 3.1.6 on 2021-04-24 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_product_count_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='count_sold',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='count sold'),
        ),
    ]
