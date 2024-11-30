from django.db import models
from django.contrib.auth.models import User
from albums.models import Album


class Favorite(models.Model):
    """
    Favorite model represents a user's favorite album. It is related to the User and Album models.

    Attributes:
    owner (models.ForeignKey): The user who owns the favorite. It is a foreign key to the User model.
    album (models.ForeignKey): The album that is favorited. It is a foreign key to the Album model.

    Meta:
    unique_together: Ensures that a user cannot have multiple favorites for the same album.

    Methods:
    __str__: Returns a string representation of the favorite in the format 'username - album title'.
    """
   
    owner = models.ForeignKey(
        User , on_delete=models.CASCADE)
    album = models.ForeignKey(
        Album, related_name="starred", on_delete=models.CASCADE
    ) 
   

    class Meta:
       
        unique_together = ['owner', 'album']

        def __str__(self):
            return f'{self.owner.username} - {self.album.title}'
