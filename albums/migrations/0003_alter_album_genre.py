# Generated by Django 5.0.6 on 2024-07-10 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_alter_genre_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='albums.genre'),
        ),
    ]