# Generated by Django 4.1.1 on 2022-11-30 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('English_App', '0028_rename_comment_createcomment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createcomment',
            name='articles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ourcomments', to='English_App.usersposts'),
        ),
    ]
