# Generated by Django 4.0.2 on 2022-03-01 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0003_remove_blogpost_content_remove_blogpost_last_updated_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPost',
            new_name='Post',
        ),
    ]
