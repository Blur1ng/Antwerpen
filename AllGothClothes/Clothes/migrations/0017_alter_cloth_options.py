# Generated by Django 4.2.16 on 2024-10-15 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clothes', '0016_cloth_brand_alter_cloth_content_alter_cloth_cost_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cloth',
            options={'ordering': ['brand']},
        ),
    ]
