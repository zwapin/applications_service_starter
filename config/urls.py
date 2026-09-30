# IMPORTING THIRD PARTY PACKAGES
from django.urls import include, path

handler404 = "mini_kit.views.not_found_view"
handler500 = "mini_kit.views.server_error_view"

urlpatterns = [
    path("api/v1/", include("rest_apis.urls")),
]
