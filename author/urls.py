from django.urls import path

from . import views

urlpatterns = [
    path('adicionar/author', views.adicionar_author, name='adicionar_author'),
]