# Generated by Django 3.2.9 on 2022-06-26 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0028_education_total_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='gpa',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
