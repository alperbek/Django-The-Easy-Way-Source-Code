# Generated by Django 2.2.5 on 2019-09-02 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_flower_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]