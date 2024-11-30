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
    Represents an album in the database.

    This model stores information about music albums, including details about 
    the album itself, the artist, and various identifiers from external 
    sources.

    Attributes:
        title (CharField): The title of the album (max length: 255 
        characters).
        artist (CharField): The name of the artist or band (max length: 255 
        characters).
        image_url (URLField): The URL of the album cover image (optional).
        release_year (SmallIntegerField): The year the album was released.
        description (TextField): A description or summary of the album 
        (optional).
        genre (CharField): The primary genre of the album (max length: 255 
        characters, optional).
        style (CharField): The specific style or subgenre of the album 
        (max length: 255 characters, optional).
        label (CharField): The record label that released the album 
        (max length: 255 characters, optional).
        album_format (CharField): The format of the album (e.g., CD, Vinyl) 
        (max length: 255 characters, optional).
        audiodb_idAlbum (IntegerField): The unique identifier for the album 
        in the AudioDB database.
        audiodb_idArtist (IntegerField): The unique identifier for the artist 
        in the AudioDB database.
        discogs_id (CharField): The unique identifier for the album in the 
        Discogs database (max length: 255 characters, optional).
        wikipedia_id (CharField): The unique identifier for the album's 
        Wikipedia page (max length: 255 characters, optional).
        created_at (DateTimeField): The date and time when the album entry 
        was created (auto-set on creation).

    Meta:
        ordering: Albums are ordered by their release year.

    Methods:
        __str__: Returns the title of the album as its string representation.
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
    audiodb_idAlbum = models.IntegerField()
    audiodb_idArtist = models.IntegerField()
    discogs_id = models.CharField(max_length=255, blank=True, null=True)
    wikipedia_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)   

    class Meta:
        ordering = ['release_year']
    def __str__(self):
        """
        Returns a string representation of the Album.

        Returns:
            str: The title of the album.
        """

        return self.title
