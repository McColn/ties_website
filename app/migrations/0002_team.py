# Generated by Django 4.2.13 on 2024-10-22 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('profile', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
