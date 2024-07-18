from django.urls import path
from favorites import views

urlpatterns = [
    path('favorites/', views.FavoriteList.as_view()),
    path('favorites/<int:pk>/', views.FavoriteDetail.as_view())
]