from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('episode/<str:episode_api_id>/',views.episode_detail, name = 'episode_detail'),
    path('character/<str:character_api_id>/', views.character_detail, name = 'character_detail'),
    path('location/<str:location_api_id>/',views.location_detail, name='location_detail'),
    path('search/',views.search,name='search'),
]