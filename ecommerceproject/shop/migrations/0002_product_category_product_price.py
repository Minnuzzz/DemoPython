# Generated by Django 5.0.1 on 2024-01-16 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=2.0, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=20.0, max_digits=10),
            preserve_default=False,
        ),
    ]