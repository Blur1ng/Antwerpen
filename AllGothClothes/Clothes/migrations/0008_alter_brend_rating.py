# Generated by Django 5.0.7 on 2024-07-28 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clothes', '0007_alter_brend_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brend',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Seller rating'),
        ),
    ]
