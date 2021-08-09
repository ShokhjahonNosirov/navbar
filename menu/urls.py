from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),    
    path('genres', views.show_genres, name = 'genres'),
]
