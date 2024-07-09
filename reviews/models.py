from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    """
    Review model, related to 'owner', i.e. a User instance.
    Relation to Album will be added later
    """
   
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
     # TODO: This should be a many-to-one relationship with Album model
    # album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='reviews', blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.SmallIntegerField()
    content = models.TextField(blank=True)
    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner.username} - {self.id}'