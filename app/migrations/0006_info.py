# Generated by Django 4.2.4 on 2023-08-14 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('company_description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
