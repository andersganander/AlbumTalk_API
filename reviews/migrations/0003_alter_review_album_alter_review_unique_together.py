# Generated by Django 5.0.6 on 2024-11-02 20:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0009_alter_album_audiodb_idalbum_and_more'),
        ('reviews', '0002_review_album'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='albums.album'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'album')},
        ),
    ]
