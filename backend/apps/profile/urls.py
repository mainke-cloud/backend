from django.urls import include, path
from apps.profile.views.profile_views import *

app_name = "profile"
urlpatterns = [
    path("", ProfileListCreateAPIView.as_view(), name="profile-list"),
    path("user/", UserListCreateAPIView.as_view(), name="profile-list"),
    path("create/", ProfileListCreateAPIView.as_view(), name="profile-create"),
    path("details/", ProfileRetrieveUpdateDestroyAPIView.as_view(), name="profile-detail"),
    path("update/<str:pk>/", ProfileRetrieveUpdateDestroyAPIView.as_view(), name="profile-update"),
    path("delete/<str:pk>/", ProfileRetrieveUpdateDestroyAPIView.as_view(), name="profile-delete"),
]