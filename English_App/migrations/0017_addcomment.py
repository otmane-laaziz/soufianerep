# Generated by Django 4.1.1 on 2022-11-18 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('English_App', '0016_alter_comment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentes', to='English_App.usersposts')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
