# Generated by Django 3.2.10 on 2022-04-03 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0003_auto_20220402_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='slug',
        ),
        migrations.AddField(
            model_name='results',
            name='year',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
