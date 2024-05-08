from django.urls import include, path
from apps.profile.views.profile_views import *

app_name = "profile"
urlpatterns = [
    path("", ProfileListCreateAPIView.as_view(), name="profile-list-create"), # filter by id_user, id_jabatan, atau id_departemen
    path("create/", ProfileListCreateAPIView.as_view(), name="profile-create"), # filter by id_user, id_jabatan, atau id_departemen
    path("update/<user_id>/", ProfileUpdateRetrieveAPIView.as_view(), name="profile-update"),

    path("sekretaris/", SekretarisListCreateAPIView.as_view(), name="sekretaris-list-create"), # filter by id_user atasan
    path("sekretaris/details/<atasan_id>/<sekretaris_id>/", SekretarisUpdateRetrieveDestroyAPIView.as_view(), name="sekretaris-update-retrieve-destroy")
]