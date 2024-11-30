from django.db import models
from django.contrib.auth.models import User
from albums.models import Album


class Review(models.Model):
    """
    Review model, related to User and Album
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE,
                              related_name='reviews', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.SmallIntegerField()
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('owner', 'album')

    def __str__(self):
        return f'{self.owner.username} - {self.id}'
