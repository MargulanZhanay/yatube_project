"""yatube URL Configuration"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


handler404 = "core.views.page_not_found"
handler500 = 'core.views.server_error'
handler403 = 'core.views.permission_denied'

urlpatterns = [
    path('', include('posts.urls', namespace='posts')),

    path('admin/', admin.site.urls),
    # We need Django to check users addresses first,
    path('auth/', include('users.urls')),
    # then if it not find some URL it would search it from django.contrib.auth
    path('auth/', include('django.contrib.auth.urls')),
    path('about/', include('about.urls', namespace='about')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
