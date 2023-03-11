from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("core_delivery.users.rest.urls")),
    path("api/", include("core_delivery.orders.rest.urls")),
    path("api/administrative/", include("core_delivery.base.rest.urls")),
]
