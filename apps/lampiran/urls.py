from django.urls import include, path
from .views import *

app_name = "lampiran"
urlpatterns = [
    path("", LampiranListCreateView.as_view(), name="lampiran-listt"),
    path("", LampiranListCreateView.as_view(), name="lampiran-create"),
    path("retrieve/<int:pk>/", LampiranRetrieveUpdateDelete.as_view(), name="lampiran-detail"),
    path("retrieve<int:pk>/", LampiranRetrieveUpdateDelete.as_view(), name="lampiran-update"),
    path("retrieve/<int:pk>/", LampiranRetrieveUpdateDelete.as_view(), name="lampiran-delete"),
]