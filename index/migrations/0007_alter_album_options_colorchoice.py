# Generated by Django 5.1.2 on 2025-01-03 12:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_alter_album_cardbody'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['photo_id']},
        ),
        migrations.CreateModel(
            name='ColorChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_id', models.IntegerField(auto_created=True, verbose_name='Color ID')),
                ('color', models.CharField(max_length=255, verbose_name='Color')),
                ('price', models.FloatField(verbose_name='Price')),
                ('cardbody', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color', to='index.cardbodies')),
            ],
            options={
                'ordering': ['color_id'],
            },
        ),
    ]
