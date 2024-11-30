from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model, representing a user's profile. It is related to the User
    model.

    """

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../media/images/default_profile2_q4xt5g'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns a string representation of the Profile object.

        The string representation is formatted as "{owner}'s profile", where
        'owner' is the username of the associated User object.

        Parameters:
        None

        Returns:
        str: A string representation of the Profile object.
        """
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Creates a Profile object when a new User object is created.

    This function is connected to the post_save signal of the User model.
    When a new User object is saved and created, a corresponding Profile object
    is created with the same owner.

    Parameters:
    sender (class): The model class sending the signal. In this case, it is
    User.
    instance (User): The instance of the User model that triggered the signal.
    created (bool): A boolean indicating whether the User object was created.
    kwargs (dict): Additional keyword arguments passed to the signal handler.

    Returns:
    None
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
