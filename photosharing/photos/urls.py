from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<int:photo_id>/', views.view, name='photo'),
    path('add/', views.add, name='add')
]
