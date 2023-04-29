"""yatube URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('posts.urls', namespace='posts')),

    path('admin/', admin.site.urls),
    # We need Django to check users addresses first,
    path('auth/', include('users.urls')),
    # then if it not find some URL it would search it from django.contrib.auth
    path('auth/', include('django.contrib.auth.urls')),
    path('about/', include('about.urls', namespace='about')),
]
