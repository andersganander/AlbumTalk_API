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
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)   

    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title




