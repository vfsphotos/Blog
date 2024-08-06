from django.urls import path

from .views import about, contact, index, post

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('post/', post, name='post'),
]
