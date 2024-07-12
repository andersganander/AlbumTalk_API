from django.db import models

class Genre(models.Model):
    """
    Genre model, related to Album
    """

    genre = models.CharField(max_length=255, default="Rock")

    def __str__(self):
        return self.genre


class Album(models.Model):
    """
    Comment model, related to User and Review
    """
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True)
    release_year = models.SmallIntegerField()
    description = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    style = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    album_format = models.CharField(max_length=255, blank=True, null=True)
    audiodb_idAlbum = models.SmallIntegerField()
    audiodb_idArtist = models.SmallIntegerField()
    discogs_id = models.CharField(max_length=255, blank=True, null=True)
    wikipedia_id = models.CharField(max_length=255, blank=True, null=True)



    created_at = models.DateTimeField(auto_now_add=True)   

    class Meta:
        ordering = ['release_year']
    def __str__(self):
        return self.title
