# Generated by Django 5.1 on 2024-08-24 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cupon',
            name='required_amount_to_use_coupon',
            field=models.PositiveBigIntegerField(default=100),
            preserve_default=False,
        ),
    ]
