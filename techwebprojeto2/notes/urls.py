from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_maestria),
    path('api/maestria/<str:summoner>', views.api_maestria_teste),
    path('api/maestria', views.api_maestria),
    path('api/fav', views.api_fav),
    path('api/fav/delete/<str:champ_id>', views.api_fav_delete),
]
