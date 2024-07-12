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
    image_url = models.URLField()
    release_year = models.SmallIntegerField()
    description = models.TextField()
    genre = models.CharField(max_length=255)
    style = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    album_format = models.CharField(max_length=255)
    audiodb_idAlbum = models.SmallIntegerField()
    audiodb_idArtist = models.SmallIntegerField()
    discogs_id = models.CharField(max_length=255, blank=True)
    wikipedia_id = models.CharField(max_length=255, blank=True)



    created_at = models.DateTimeField(auto_now_add=True)   

    class Meta:
        ordering = ['release_year']
    def __str__(self):
        return self.title
