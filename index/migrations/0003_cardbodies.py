# Generated by Django 5.1.4 on 2024-12-23 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardBodies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('sizes', models.CharField(max_length=255, verbose_name='Sizes')),
                ('price', models.FloatField(verbose_name='Price')),
                ('photo', models.FileField(upload_to='cards/', verbose_name='Photo')),
                ('date', models.DateField(verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Card Body',
                'verbose_name_plural': 'Card Bodies',
            },
        ),
    ]