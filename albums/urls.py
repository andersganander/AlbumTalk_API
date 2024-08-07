from django.urls import path
from albums import views

urlpatterns = [
    path('albums/', views.AlbumList.as_view()),
    path('albums/<int:pk>/', views.AlbumDetail.as_view()),
    path('albums/import', views.import_data)
]