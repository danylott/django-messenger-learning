from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("messenger/", include("messenger.urls", namespace="messenger")),

    path("__debug__/", include("debug_toolbar.urls")),
]
