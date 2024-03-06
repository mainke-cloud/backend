from django.urls import include, path
from apps.departemen.views import *

app_name = "departemen"
urlpatterns = [
    path("", DepartemenListCreateAPIView.as_view(), name="departemen-list"),
    path("create/", DepartemenListCreateAPIView.as_view(), name="departemen-create"),
    path("detail/<str:id_departemen>/", DepartemenRetrieveUpdateDestroyAPIView.as_view(), name="departemen-detail"),
    path("detail/<str:id_departemen>/", DepartemenRetrieveUpdateDestroyAPIView.as_view(), name="departemen-update"),
    path("detail/<str:id_departemen>/", DepartemenRetrieveUpdateDestroyAPIView.as_view(), name="departemen-delete"),
]