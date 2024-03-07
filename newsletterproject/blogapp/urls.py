from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path("blog/<slug:slug>/", views.blog, name='blog'),
]
