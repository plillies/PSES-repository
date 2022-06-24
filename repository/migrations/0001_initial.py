# Generated by Django 3.2.10 on 2022-04-02 17:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Summary', max_length=250)),
                ('code', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=4)),
                ('slug', models.SlugField(max_length=250)),
                ('file', models.FileField(upload_to='data/%year')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
