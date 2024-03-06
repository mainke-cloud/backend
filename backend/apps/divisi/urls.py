from django.urls import include, path
from apps.divisi.views import *

app_name = "divisi"
urlpatterns = [
    path("", DivisiListCreateAPIView.as_view(), name="divisi-list"),
    path("create/", DivisiListCreateAPIView.as_view(), name="divisi-create"),
    path("detail/<str:id_divisi>/", DivisiRetrieveUpdateDestroyAPIView.as_view(), name="divisi-detail"),
    path("detail/<str:id_divisi>/", DivisiRetrieveUpdateDestroyAPIView.as_view(), name="divisi-update"),
    path("detail/<str:id_divisi>/", DivisiRetrieveUpdateDestroyAPIView.as_view(), name="divisi-delete"),
]