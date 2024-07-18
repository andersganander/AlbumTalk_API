from django.db import models
from django.contrib.auth.models import User
from albums.models import Album


class Favorite(models.Model):
    """
    Favorite model, related to user and album.
    """
   
    owner = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE) 
   

    class Meta:
        #ordering = ['owner.username']
        unique_together = ['owner', 'album']

    def __str__(self):
        return f'{self.owner.username} - {self.album.title}'

    #TODO Add signal so that a favorite is created when profile is edited