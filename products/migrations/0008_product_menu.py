# Generated by Django 3.1.6 on 2021-04-07 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_product_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.menu'),
        ),
    ]
