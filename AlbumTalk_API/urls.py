"""
URL configuration for AlbumTalk_API project.
"""
from django.contrib import admin
from django.urls import path, include
from .views import root_route

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),

    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),


    path('', include('profiles.urls')),
    path('', include('reviews.urls')),
    path('', include('comments.urls')),
    path('', include('albums.urls')),
    path('', include('followers.urls')),
    path('', include('favorites.urls')),
    
    path('', root_route),
]
