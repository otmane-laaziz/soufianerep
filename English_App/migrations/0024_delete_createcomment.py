# Generated by Django 4.1.1 on 2022-11-19 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('English_App', '0023_rename_article_createcomment_articles'),
    ]

    operations = [
        migrations.DeleteModel(
            name='createComment',
        ),
    ]
