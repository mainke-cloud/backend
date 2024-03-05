from django.urls import include, path
from apps.profile.views import *

app_name = "profile"
urlpatterns = [
    path("", ProfileListCreateAPIView.as_view(), name="profile-list"),
    path("create/", ProfileListCreateAPIView.as_view(), name="profile-create"),
    path("<str:id_profile>/", ProfileRetrieveUpdateDestroyAPIView.as_view(), name="profile-detail"),
    path("<str:id_profile>/", ProfileRetrieveUpdateDestroyAPIView.as_view(), name="profile-update"),
    path("<str:id_profile>/", ProfileRetrieveUpdateDestroyAPIView.as_view(), name="profile-delete"),
]