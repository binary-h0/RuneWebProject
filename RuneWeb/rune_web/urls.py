from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('cardinfo/', views.cardinfo, name='cardinfo'),
    path('deckbuilder/', views.deckbuilder, name='deckbuilder'),
    path('community/', views.community, name='community'),
]