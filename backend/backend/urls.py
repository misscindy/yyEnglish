"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles import views as static_views
from django.urls import path, re_path

from backend import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'v0', include('api.urls', namespace='api')),
    re_path(r'^o/',
            include('oauth2_provider.urls', namespace='oauth2_provider')),

    re_path(r'^(?i)media/(?P<path>.*)$', static_views.static.serve,
            {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^(?i)upload/(?P<path>.*)$', static_views.static.serve,
            {'document_root': settings.MEDIA_UPLOAD}),
]

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^(?i)static/(?P<path>.*)$', static_views.static.serve,
                {'document_root': settings.STATIC_ROOT}),
    ]
