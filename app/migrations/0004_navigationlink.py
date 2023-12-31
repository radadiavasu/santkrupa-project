# Generated by Django 4.2.4 on 2023-08-13 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='navigation_links', to='app.header')),
            ],
        ),
    ]
