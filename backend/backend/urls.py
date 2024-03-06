from django.contrib import admin
from django.urls import path, include
from apps.profile.views.auth_views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include([
        path('profile/', include('apps.profile.urls')),
        path('divisi/', include('apps.divisi.urls')),
        path('departemen/', include('apps.departemen.urls')),
        path('jabatan/', include('apps.jabatan.urls')),
        path(
        "auth/",
        include(
            [
                path("login/", LoginView.as_view(), name="auth-login"),
                path("register/", RegisterView.as_view(), name="auth-register"),
                path("logout/", LogoutView.as_view(), name="auth-logout"),
            ]
        ),
    ),
    ])),
]
