from django.urls import include, path
from apps.jabatan.views import *

app_name = "jabatan"
urlpatterns = [
    path("", JabatanListCreateAPIView.as_view(), name="jabatan-list"),
    path("create/", JabatanListCreateAPIView.as_view(), name="jabatan-create"),
    path("detail/<str:id_jabatan>/", JabatanRetrieveUpdateDestroyAPIView.as_view(), name="jabatan-detail"),
    path("detail/<str:id_jabatan>/", JabatanRetrieveUpdateDestroyAPIView.as_view(), name="jabatan-update"),
    path("detail/<str:id_jabatan>/", JabatanRetrieveUpdateDestroyAPIView.as_view(), name="jabatan-delete"),
]