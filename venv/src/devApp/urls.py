# Je fais mes chemin vers les pages de mon app
from django.urls import path
from . import views
urlpatterns = [
    path('', views.dev, name="index"),
]

