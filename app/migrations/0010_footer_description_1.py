# Generated by Django 4.2.4 on 2023-08-14 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='description_1',
            field=models.URLField(blank=True, default=1),
        ),
    ]