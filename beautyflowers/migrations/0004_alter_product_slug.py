# Generated by Django 4.0.2 on 2022-03-12 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautyflowers', '0003_alter_product_image_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]