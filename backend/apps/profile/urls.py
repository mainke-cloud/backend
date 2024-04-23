from django.urls import include, path
from apps.profile.views.profile_views import *

app_name = "profile"
urlpatterns = [
    path("", ProfileAPIView.as_view(), name="my-profile"),
    path("update/", ProfileUpdateAPIView.as_view(), name="profile-update"),
]