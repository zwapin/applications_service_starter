# IMPORTING THIRD PARTY PACKAGES
from django.urls import path

# IMPORTING LOCAL PACKAGES
from rest_apis.views import SingleStoreApiView, StoresApiView

app_name = "rest_apis"

urlpatterns = [
    path("stores", StoresApiView.as_view()),
    path("stores/<int:store_pk>", SingleStoreApiView.as_view()),
]
