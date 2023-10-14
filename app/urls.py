from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('templates/index.html', views.index, name='index'),
    path('templates/about.html', views.about, name='about'),
    path('templates/gallery.html', views.gallery, name='gallery'),
    path('templates/service.html', views.service, name='service'),
    path('templates/blog.html', views.blog, name='blog'),
    path('templates/contact.html', views.contact, name='contact'),
]    

