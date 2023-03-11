from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("core_delivery.users.rest.urls")),
    path("api/v1/", include("core_delivery.orders.rest.urls")),
    path("api/administrative/", include("core_delivery.base.rest.urls")),

    path("api/obtain/", TokenObtainPairView.as_view(), name="jwt_pair"),
    path("api/refresh/", TokenRefreshView.as_view(), name="jwt_refresh")

]
