# Generated by Django 5.0.6 on 2024-07-12 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0004_alter_album_options_remove_album_release_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='discogs_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='wikipedia_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
