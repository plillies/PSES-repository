# Generated by Django 3.2.10 on 2022-04-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_alter_results_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='language',
            field=models.CharField(default='en', max_length=2),
        ),
    ]