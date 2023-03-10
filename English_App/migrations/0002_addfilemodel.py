# Generated by Django 4.1.1 on 2022-09-25 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('English_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('pdf', models.FileField(upload_to='pdfs/%y')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
