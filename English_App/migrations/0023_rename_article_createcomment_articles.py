# Generated by Django 4.1.1 on 2022-11-19 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('English_App', '0022_rename_post_addcomment_posts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createcomment',
            old_name='article',
            new_name='articles',
        ),
    ]
