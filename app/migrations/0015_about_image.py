# Generated by Django 4.2.4 on 2023-08-14 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
        ),
    ]