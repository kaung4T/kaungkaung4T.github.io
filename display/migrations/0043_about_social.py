# Generated by Django 3.2.9 on 2023-03-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0042_auto_20230207_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='social',
            field=models.URLField(blank=True, null=True),
        ),
    ]
