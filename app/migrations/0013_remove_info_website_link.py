# Generated by Django 4.2.4 on 2023-08-14 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_rename_company_name_link_info_website_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='website_link',
        ),
    ]