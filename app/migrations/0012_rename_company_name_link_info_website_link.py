# Generated by Django 4.2.4 on 2023-08-14 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_info_company_name_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='company_name_link',
            new_name='website_link',
        ),
    ]