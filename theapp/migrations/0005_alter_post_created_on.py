# Generated by Django 4.0.2 on 2022-03-01 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0004_rename_blogpost_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateField(blank=True, null=True),
        ),
    ]
