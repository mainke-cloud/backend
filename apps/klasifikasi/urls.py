from django.urls import include, path
from apps.klasifikasi.views import *

app_name = "klasifikasi"
urlpatterns = [
    path("", KlasifikasiListCreateAPIView.as_view(), name="klasifikasi-list"),
    path("", KlasifikasiListCreateAPIView.as_view(), name="klasifikasi-create"),
    path("retrieve/<str:pk>/", KlasifikasiRetrieveUpdateDestroyAPIView.as_view(), name="klasifikasi-detail"),
    path("retrieve/<str:pk>/", KlasifikasiRetrieveUpdateDestroyAPIView.as_view(), name="klasifikasi-update"),
    path("retrieve/<str:pk>/", KlasifikasiRetrieveUpdateDestroyAPIView.as_view(), name="klasifikasi-delete"),
]