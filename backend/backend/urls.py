"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include([
        path('profile/', include('apps.profile.urls')),
        path('divisi/', include('apps.divisi.urls')),
        path('departemen/', include('apps.departemen.urls')),
        path('jabatan/', include('apps.jabatan.urls')),
        # path("login/", admin.site.urls),
        # path("register/", admin.site.urls),
        path('lampiran/', include('apps.lampiran.urls')),
        path('surat/', include('apps.surat.urls')),
        path('group/', include('apps.group.urls')),
    ])),
]
