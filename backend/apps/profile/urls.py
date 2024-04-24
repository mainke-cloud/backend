from django.urls import include, path
from apps.profile.views.profile_views import *

app_name = "profile"
urlpatterns = [
    path("", ProfileListCreateAPIView.as_view(), name="profile-list"), # bisa filter by id_user
    path("create/", ProfileListCreateAPIView.as_view(), name="profile-create"), # bisa filter by id_user
    path("update/<user_id>", ProfileUpdateRetrieveAPIView.as_view(), name="profile-update")
]